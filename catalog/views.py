from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect, Http404
from django.http import HttpResponseNotFound
import logging
from catalog.models import Movie


logger = logging.getLogger('movie_logger')

CATEGORIES = (
    "action",
    "comedy",
    "tv_shows"
)


def index(request):
    logger.info("Start application")
    return render(request, "base.html")


def catalog_view(request):
    movies = Movie.objects.all()
    context = {
        "movies": movies
    }
    return render(request, "movies.html", context=context)


def catalog_detail_view(request, cat):
    if cat not in CATEGORIES:
        return redirect('home', permanent=True)
    return HttpResponse(f'<h3>Main paige</h3>{cat}</p>')


def movie_detail_view(request, cat, mov_id):
    return HttpResponse(f'<h3>{cat}</h3>{mov_id}</p>')


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h3>Page not found</h3>")
