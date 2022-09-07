from django.shortcuts import render, HttpResponse

def wish_1(request):
	return HttpResponse('<h1> Hello from firstapp </h1>')
