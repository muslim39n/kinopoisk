from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import *
from django.shortcuts import render, get_object_or_404


def index(request):
    movies = Movie.objects.order_by('movie_main_rating')

    return render(request, "mainapp/index.html", {'movies':movies})


def movie(request, movie_id):
    moviex = get_object_or_404(Movie, pk=movie_id)

    return render(request, "mainapp/movie.html", {'movie': moviex})

# Create your views here.
