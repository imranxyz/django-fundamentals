from django.urls import path 
from . import views 

urlpatterns = [
	path('', views.home, name='home'),
	path('add-movie/', views.addMovie, name='add-movie'),
	path('list-of-movies/', views.listOfMovies, name='list-of-movies')
]