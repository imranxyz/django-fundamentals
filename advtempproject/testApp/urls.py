from django.urls import path 
from . import views 

urlpatterns = [
	path('', views.homeView, name='home'),
	path('movies/', views.movies, name='movies'),
	path('politics/', views.politics, name='politics'),
	path('sports/', views.sports, name='sports'),
]