from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('movies/', views.movies, name='movies'),
	path('news/', views.news, name='news'),
]