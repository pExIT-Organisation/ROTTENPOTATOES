from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .models import Movie


def list_of_movies(request):
    all_movies = Movie.movies_manager.all()
    return render(request, 'movies.html', {'all': all_movies})


def movie_detail(request, movie_name):
    all_movies = Movie.movies_manager.all()
    try:
        movie = all_movies.get(name=movie_name)
    except ObjectDoesNotExist:
        movie = None

    context = {'movie': movie}
    return render(request, 'movie_details.html', context)
