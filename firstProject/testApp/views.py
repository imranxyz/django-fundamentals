from django.shortcuts import render, HttpResponse

def welcome(request):
	return HttpResponse('<h1> welcome to django </h1>')
