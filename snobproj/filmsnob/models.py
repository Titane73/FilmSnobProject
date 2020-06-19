from django.db import models
from django.contrib.auth.models import User

# First model here
class Movies(models.Model):
    G = 'G'
    PG = 'PG'
    PG13 ='PG-13'
    R = 'R'
    RATING_OPTIONS = [
        (G, 'G'),
        (PG, 'PG'),
        (PG13, 'PG-13'),
        (R, 'R'),
    ]

    movie_title = models.CharField(max_length = 125)
    movie_release = models.DateField()
    movie_director = models.CharField(max_length = 70)
    movie_length = models.CharField(max_length = 12)
    movie_rating  = models.CharField(
        max_length = 5,
        choices = RATING_OPTIONS,
        default = PG,
    )
    movie_summary = models.TextField()
    
    def __str__(self):
        return self.movie_title
    
    class Meta:
        db_table = 'movie'
        verbose_name_plural = 'movies'

class Review(models.Model):
    EXCEPTIONAL = 'A'
    ENTERTAINING = 'B'
    AMUSING = 'C'
    TOLERABLE = 'D'
    REGRETTABLE = 'E'

    RATINGS = [
        (EXCEPTIONAL, 'Exceptional'),
        (ENTERTAINING, 'Entertaining'),
        (AMUSING, 'Amusing'),
        (TOLERABLE, 'Tolerable'),
        (REGRETTABLE, 'Regrettable'),
    ]

    review_title = models.CharField(max_length = 125)
    movie = models.ForeignKey(Movies, on_delete = models.CASCADE)
    review_date = models.DateField()
    review_rating = models.CharField(
        max_length = 15,
        choices = RATINGS,
        default = ENTERTAINING,
    )
    review_text = models.TextField(blank = True)

    def __str__(self):
        return self.review_title

    class Meta:
        db_table = 'review'
        verbose_name_plural = 'reviews'
    

