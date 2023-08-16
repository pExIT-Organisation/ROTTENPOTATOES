from django.urls import path
from . import views

urlpatterns = [
    path('movie-list/', views.list_of_movies, name="movie-list"),
    path('movie/<str:movie_name>/', views.movie_detail, name='movie_detail'),
]
