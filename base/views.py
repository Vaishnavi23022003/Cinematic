from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Movie
from .models import Rating
from .models import Customer
from django.contrib.auth.models import User
from operator import itemgetter,attrgetter
import pandas as pd
import numpy as np
import threading


def predict_rating(similar_users, row):
    # function to predict rating at a movie
    # row represents the ratings given to the movie by all the users
    rating_sum = 0
    similarity_sum = 0

    for user in similar_users.iteritems():
        rating_sum += row[user[0]] * user[1]
        similarity_sum += user[1]
    if similarity_sum == 0:
        return 0
    return rating_sum / similarity_sum


def get_similar_user_movies(user_similarity, movie_ratings, user_name):
    try:
        # fetching the Pearson correlation coefficients for similarity
        # between user with user_name and other users
        similar_users = user_similarity[user_name]
    except Exception as e:
        print(e)
        return []

    # this sorting will result in most similar users at the beginning
    # and least similar at the end
    similar_users = similar_users.sort_values(ascending=False)

    # selecting only top 6 similar users
    similar_users = similar_users.drop(similar_users.index[range(7, 610)])

    # since the user will be most similar to him/her self,
    # dropping them from the similar users
    similar_users = similar_users.drop(similar_users.index[0])

    predicted_ratings = []
    movie_ids = []

    # predicting rating for each movie not watched by the user
    for item, row in movie_ratings.iterrows():

        # true if movie is not watched/rated by the user
        if row[user_name] == 0.0:
            # predict_rating return the predicted rating of the movie
            predicted_ratings.append(predict_rating(similar_users, row))
            movie_ids.append(item)

    # creating top_movies panda series using predicted_ratings(values) list and movie_ids (index)
    top_movies = pd.Series(np.array(predicted_ratings), index=movie_ids)

    # sorting the movies on the basis of predicted rating in reverse order
    top_movies = top_movies.sort_values(ascending=False)
    # keeping only top 50 movies and dropping others
    top_movies = top_movies.drop(top_movies.index[range(50, len(movie_ids))])
    return top_movies


def get_recommendation(user_name):
    # reading ratings file:
    ratings = pd.DataFrame(list(Rating.objects.all().values()))

    # reding movies file:
    movies = pd.DataFrame(list(Movie.objects.all().values()))

    # merging the ratings and movies dataframes
    ratings = pd.merge(movies, ratings)

    # creating a new dataframe with user_name as column and movie_id as row
    # movie_ratings[i][j] = rating given to movie i by user j
    movie_ratings = ratings.pivot_table(index=['movie_id'], columns=['user_name'], values='rating').fillna(0)

    # calculating the user_similarity Correlation matrix using pearson similarity
    # user_similarity[i][j] represents the Pearson correlation coefficient between user i and j
    # i.e. how similar user i and j are
    user_similarity = movie_ratings.corr(method='pearson')

    # converting user_similarity Correlation matrix to panda dataframe
    user_similarity = pd.DataFrame(user_similarity, index=movie_ratings.columns, columns=movie_ratings.columns)

    # fetching movies watched by users similar to user with user_name
    similar_user_movies = get_similar_user_movies(user_similarity, movie_ratings, user_name)

    if len(similar_user_movies) == 0:
        return []

    recommendations = []
    for i in similar_user_movies.iteritems():
        recommendations.append(i[0])

    # saving list of recommended movie_ids as a string where two movie_ids are separated by '|'
    s = "|"
    s = s.join([str(k) for k in recommendations])
    user = User.objects.get(username=user_name)
    movie_obj = Customer.objects.get(user=user)
    movie_obj.recommendations = s
    print(s)
    movie_obj.save()


def get_popular(user_name):
    # fetching all the movies as a panda dataframe
    ratings = pd.DataFrame(list(Movie.objects.all().values()))

    avg_rating = []
    for item, row in ratings.iterrows():
        # movies which are rated by more than 100 users are appended into avg_rating list
        if row['ratings_total'] < 100:
            continue
        # calculating the average rating of the movie
        avg_rating.append([row['ratings_val'] / row['ratings_total'], row['movie_id']])

    # sorting movies on the basis of their average rating in reverse order
    avg_rating = sorted(avg_rating, key=itemgetter(0), reverse=True)

    popular = []
    k = 0
    # taking only top 50 movies
    for i in range(len(avg_rating)):
        if k >= 50:
            break
        if Rating.objects.filter(movie_id=avg_rating[i][1], user_name=user_name).count() != 0:
            continue
        popular.append(avg_rating[i][1])
        k += 1
        print(avg_rating[i][0])

    #saving list of popular movie's movie_ids as a string where two movie_ids are separated by '|'
    s = "|"
    s = s.join([str(k) for k in popular])
    user = User.objects.get(username=user_name)
    movie_obj = Customer.objects.get(user=user)
    movie_obj.recommendations = s
    movie_obj.save()


def get_watched(user_name):
    # fetching all the movies watched/rated by the user
    watched_movies = Rating.objects.filter(user_name=user_name)
    # sorting the movies on the bases of rating given by user in reverse order
    watched_movies=sorted(watched_movies,key=attrgetter('rating'),reverse=True)
    watched_ids = []

    i = 0
    # taking only top 20 movies
    for k in watched_movies:
        if i >= 12:
            break
        m = Movie.objects.get(movie_id=int(k.movie_id))
        if m.poster == "" or m.genre is None:
            continue
        watched_ids.append(m)
        i += 1
    return watched_ids


def get_movie_data(movies, max_len):
    # converting the movie string which contains movie_ids where two movie ids are separated by '|'
    # into a list that contains movies(Movie Model object)
    movie_data = []
    cnt = 1
    for m in movies:
        if cnt == max_len or cnt == 50:
            break
        if m.poster == "" or m.genre is None:
            continue
        s = m.genre.split('|')
        s = s[:min(2, len(s))]
        s = ' '.join(s)
        m.genre = s
        s = m.title
        if len(s) > 40:
            s = s[:40]
            s += "..."
            m.title = s
        movie_data.append(m)
        cnt += 1
    return movie_data


# backdrop_url = "http://image.tmdb.org/t/p/original"+backdrop_path
# poster_url = "http://image.tmdb.org/t/p/w500" + poster_path


def login_user(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username/Password is incorrect')

    context = {'page': page}
    return render(request, 'base/auth.html', context)


def logout_user(request):
    logout(request)
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        user = User(username=username, password=password)
        user.username = user.username.lower()
        customer = Customer(user=user, rated=0, recommendations="")
        user.save()
        customer.save()
        get_popular(user.username)
        login(request, user)
        return redirect('home')

    return render(request, 'base/auth.html')


@login_required(login_url='login')
def home(request):
    movies = []
    if request.GET.get('q') is not None:
        q = request.GET.get('q')
        movies = Movie.objects.filter(title__icontains=q)
    else:
        movie_obj = Customer.objects.get(user_id=request.user.id)
        recc = list(movie_obj.recommendations.split("|"))
        if recc!='':
            for i in recc:
                movies.append(Movie.objects.get(movie_id=int(i)))

    try:
        movies = get_movie_data(movies, 25)
        watched = get_watched(request.user.username)
        watched = get_movie_data(watched, 13)
        context = {'movies': movies,
                   'poster': movies[0].backdrop,
                   'not_avail': False,
                   'watched': watched}
    except:
        context = {'movies': movies,
                   'poster': '/3s9O5af2xWKWR5JzP2iJZpZeQQg.jpg',
                   'not_avail': True,
                   'watched': watched}

    return render(request, 'base/home.html', context)


@login_required(login_url='login')
def movie(request, pk):
    username = request.user.username
    user = User.objects.get(username=username)
    customer = Customer.objects.get(user=user)
    try:
        rating = Rating.objects.filter(user_name=username,
                                       movie_id=int(pk))
        rating = rating[0]
        old_rate = rating.rating
    except Exception as e:
        old_rate = 0

    if request.method == 'POST':
        print(request.POST.get('stars'))
        stars = int(request.POST.get('stars'))
        if old_rate != 0:
            rating.rating = stars
            rating.save()
            rated_movie = Movie.objects.get(movie_id=int(pk))
            rated_movie.ratings_val = rated_movie.ratings_val + stars - old_rate
            rated_movie.save()
            old_rate = rating.rating
        else:
            rating = Rating(user_name=username,
                            movie_id=int(pk),
                            rating=stars)
            rating.save()
            customer.rated = customer.rated + 1
            customer.save()
            rated_movie = Movie.objects.get(movie_id=int(pk))
            rated_movie.ratings_val = rated_movie.ratings_val + stars
            rated_movie.ratings_total += 1
            old_rate = rating.rating
            rated_movie.save()

        if customer.rated >= 20:
            print("Finding new recommendations ...")
            t1 = threading.Thread(target=get_recommendation, args=username)
            t1.setDaemon(True)
            t1.start()
        else:
            get_popular(user_name=username)

    movie_obj = Movie.objects.get(movie_id=pk)
    g = movie_obj.genre
    movie_obj.genre = g[:len(g) - 1]
    temp = list(movie_obj.recommendations.split("|"))
    recc = []
    for i in temp:
        recc.append(Movie.objects.get(movie_id=int(i)))

    recc = get_movie_data(recc, 25)
    watched = get_watched(username)
    watched = get_movie_data(watched, 13)

    context = {'movie': movie_obj,
               'recommendations': recc,
               'id': pk,
               'rating': int(old_rate),
               'watched': watched}
    return render(request, 'base/movie.html', context)
