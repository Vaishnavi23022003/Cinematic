from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rated = models.IntegerField(default=0)
    recommendations = models.TextField(default=None)

    def __str__(self):
        return self.user.username


class Movie(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    recommendations = models.TextField(default=None)
    ratings_val = models.DecimalField(max_digits=10, decimal_places=2)
    ratings_total = models.DecimalField(max_digits=10, decimal_places=2)

    poster=models.CharField(max_length=200)
    backdrop=models.CharField(max_length=200)
    release_date=models.CharField(max_length=200)
    overview=models.TextField(default=None)
    youtube_id=models.CharField(max_length=200)
    genre=models.CharField(max_length=200,default=None)

    def __str__(self):
        return self.title


class Rating(models.Model):
    user_name = models.CharField(max_length=200)
    movie_id = models.IntegerField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return f"{self.rating}"
