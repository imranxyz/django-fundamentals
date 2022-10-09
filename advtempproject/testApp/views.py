from django.shortcuts import render


def homeView(request):
	return render(request, 'testApp/home.html')

def politics(request):
	return render(request, 'testApp/politics.html')

def movies(request):
	return render(request, 'testApp/movies.html')	

def sports(request):
	return render(request, 'testApp/sports.html')	