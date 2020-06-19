from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('getMovies/', views.getMovies, name = 'movies'),
    path('getReview/<int:id>', views.getReview, name = 'review'),
    path('newMovie/', views.newMovie, name = 'newmovie'),
    path('newReview/', views.newReview, name = 'newreview'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),


]