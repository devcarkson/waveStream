from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('movies/', views.movies, name='movies'),
    path('nollywood/', views.nollywood, name='nollywood'),
    path('movie/<slug:slug>/', views.movie_detail, name='movie_detail'),
    path('toggle_favorite/', views.toggle_favorite, name='toggle_favorite'),
    path('favorites/', views.favorite_movies, name='favorite_movies'),
    path('series/', views.series, name='series'),
    path('search/', views.search, name='search'),
]
