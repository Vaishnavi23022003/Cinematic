# Cinematic
A movie-recommendation website built using python django framework. [Website Link](https://cinematic2022.herokuapp.com)

### Prerequisites
Git
Python (version 3 or above)

### Setup

```sh
$ git clone https://github.com/Vaishnavi23022003/Cinematic.git
$ cd Cinematic
```

Create a virtual environment to install dependencies in:

```sh
$ python -mvenv env
```
if above command does not work due to difference in python versions try:
```sh
$ pip install virtaulenv
$ virtualenv env
```

Activate the virtual environment
```sh
$ env/scripts/activate
```
if above command does not work due to difference in python versions try:
```sh
$ source env/bin/activate
```
if it still doesn't work then find the activate file in env folder and use it's path


Then install the dependencies:
```sh
(env)$ pip install -r requirements.txt
```
if above command does not work due to difference in python versions try:
use `py -m pip install` in place of  `pip install`

Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ pip install django
(env)$ django-admin startproject temp
```

A temp folder will be created -> we only need this for django `SECRET_KEY`.<br />
Go to `temp/temp/settings.py` and copy the value of `SECRET_KEY`.<br />
Now got to `../../Cinematic/settings.py` and replace the value of `SECRET_KEY` with the copied one.<br />
Also change `<db_user_name>` with the name of postgresql database and `<db_password>` with password of postgresql database.

Now:
```sh
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000`

### Features
1. **Recommendation** When a user logins to the website, the following happens:<br />
  * if the user has rated more than 20 movies
    *  the app recommends movie using [user based collborative filtering](https://www.geeksforgeeks.org/user-based-collaborative-filtering/)
  * else
    * the app recommends movie using [popularity based filtering](https://www.analyticssteps.com/blogs/what-are-recommendation-systems-machine-learning)
2. **Search** In the home page the user can search movies and movies with similar names will appear.
3. **Movie** When user clicks on a movie it loads the page for that movie which contains details ragarding that movie.
4. **Similar Movies** The movie page also contains movies similar to the selected movie based on genre using [content based filtering](https://www.educative.io/edpresso/what-is-content-based-filtering)
5. **Trailer** When user clicks on the trailer button the app plays the trailer of that movie.
6. **Watch Again** A lot of times users like to watch movies again. So the app also has a Watch Again section <br/> where the movies are displayed in a sorted order on the basis of the rating given by the user in reverse order.

### Screenshots of website

The authentication page. </br>
![p](https://i.ibb.co/X5cGRC7/p.png)</br></br>
The home page -> contains reccomendations</br>
![p](https://i.ibb.co/Z8cDP0Z/Cinematic-Firefox-Developer-Edition-28-05-2022-20-30-56.png)</br></br>
The Movie page</br>
![p](https://i.ibb.co/X4xqwQD/Cinematic-Firefox-Developer-Edition-28-05-2022-20-34-19.png)</br></br>
On pressing the trailer button, the trailer of the movie is played</br>
![p](https://i.ibb.co/YRPPKr4/Cinematic-Firefox-Developer-Edition-28-05-2022-20-34-27.png)</br></br>
Similar Movies Section</br>
![p](https://i.ibb.co/yFkbDcS/Cinematic-Firefox-Developer-Edition-28-05-2022-20-35-07.png)</br></br>
Watch Again Section</br>
![p](https://i.ibb.co/CBy0WLv/Cinematic-Firefox-Developer-Edition-28-05-2022-20-35-17.png)</br></br>








