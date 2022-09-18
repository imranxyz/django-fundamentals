from django.shortcuts import render


def home(request):
	context = {

	}
	return render(request, 'testApp/home.html', context)


def news(request):
	context = {
	
	}
	return render(request, 'testApp/news.html', context)


def movies(request):
	context = {
	
	}
	return render(request, 'testApp/movies.html', context)