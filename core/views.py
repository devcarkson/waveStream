from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from . models import *
from django.db.models import Q

from django.views.decorators.http import require_POST
from django.http import JsonResponse
import json
from django.conf import settings


def index(request):
    movies = movie.objects.all()
    casts = cast.objects.all()
    movies_list = movie.objects.all()
    paginator = Paginator(movies_list, 4) 
    home = list(movie.objects.all().values('id', 'name', 'image', 'video', 'slug', 'tag1', 'tag2', 'tag3'))
    for movie_data in home:
        movie_data['image_url'] = settings.MEDIA_URL + movie_data['image']
        movie_data['video_url'] = settings.MEDIA_URL + movie_data['video']


    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'casts': casts,
        'movies': movies,
        'movies_json': json.dumps(home),
    }
    return render(request, 'index.html',context)


def movies(request):
    movies_list = movie.objects.all()
    paginator = Paginator(movies_list, 16) 

    page_number = request.GET.get('page')
    page_ = paginator.get_page(page_number)
    context = {
        'page_': page_,
        'movies': page_.object_list, 
    }
    return render(request, 'movies.html', context)




def search(request):
    query = request.GET.get('query', '')
    if query:
        results = movie.objects.filter(
            Q(name__icontains=query) |
            Q(tag1__icontains=query) |
            Q(tag2__icontains=query) |
            Q(tag3__icontains=query)
        )
    else:
        results = []
    
    context = {
        'results': results,
        'query': query,
    }
    return render(request, 'search.html', context)



def series(request):
    context = {
        
    }
    return render(request, 'series.html', context)



def movie_detail(request, slug):
    movie_instance = get_object_or_404(movie, slug=slug) 
    related_movies = movie_instance.get_related_movies() 
    casts = cast.objects.filter(movie=movie_instance)
    context = {
        'movies': movie_instance,
        'casts': casts,
        'related_movies': related_movies,
    }
    return render(request, 'movie_detail.html', context)



def nollywood(request):
    nolly = movie.objects.filter(
        Q(name__icontains='nollywood') |
        Q(tag1__icontains='nollywood') |
        Q(tag2__icontains='nollywood') |
        Q(tag3__icontains='nollywood') |
        Q(name__icontains='Nollywood') |
        Q(tag1__icontains='Nollywood') |
        Q(tag1__icontains='Action') |
        Q(tag2__icontains='Nollywood') |
        Q(tag3__icontains='Nollywood')
    )

    paginator = Paginator(nolly, 16) 
    page_number = request.GET.get('page')
    page_o = paginator.get_page(page_number)

    context = {
        'page_o': page_o,
        'nolly': page_o.object_list,
    }
    return render(request, 'nollywood.html', context)


@require_POST
def toggle_favorite(request):
    movie_id = request.POST.get('movie_id')
    movie = get_object_or_404(movie, id=movie_id)
    session_id = request.session.session_key

    if not session_id:
        request.session.create()
        session_id = request.session.session_key

    favorite, created = Favorite.objects.get_or_create(session_id=session_id, movie=movie)
    
    if created:
        # New favorite was created
        return JsonResponse({'status': 'added'})
    else:
        # Favorite already existed, so remove it
        favorite.delete()
        return JsonResponse({'status': 'removed'})


def favorite_movies(request):
    session_id = request.session.session_key
    if not session_id:
        request.session.create()
        session_id = request.session.session_key

    favorites = Favorite.objects.filter(session_id=session_id).select_related('movie')
    favorite_movies = [favorite.movie for favorite in favorites]
    context = {
        'favorite_movies': favorite_movies
    }
    return render(request, 'favorite_movies.html', context)
