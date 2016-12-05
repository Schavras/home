from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Movie


def index(request):
    movies = Movie.objects.order_by('year', 'title')
    context = {
        'list_movies': movies
    }
    return render(request, 'index.html', context)
    # return HttpResponse("Hello, world. You are at the djbr index.")


def movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movie.html', {'movie': movie})


def watch(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'watch.html', {'movie': movie})
