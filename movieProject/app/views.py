from django.shortcuts import render, redirect
from . import forms, models


def home(request):
	return render(request, 'app/home.html')


def addMovie(request):
	form = forms.MovieForm()

	if request.method == 'POST':
		form = forms.MovieForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')

	return render(request, 'app/addMovie.html', context={
			'form': form, 
		})


def listOfMovies(request):
	movies = models.Movie.objects.all() # grab all the data from database
	return render(request, 'app/listOfMovies.html', context={
			'movies': movies,
		})