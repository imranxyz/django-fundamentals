from django.shortcuts import render, HttpResponse

# Create your views here.
def wish_2(request):
	return HttpResponse('<h1> Hello from secondapp </h1>')