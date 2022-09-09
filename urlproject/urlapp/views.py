from django.shortcuts import render, HttpResponse


def hydjobs(request):
	return HttpResponse('<h1> Hyderbad Jobs Information </h1>')


def chennaijobs(request):
	return HttpResponse('<h1> Chennai Jobs Information </h1>')


def kolkatajobs(request):
	return HttpResponse('<h1> Kolkata Jobs Information </h1>')


def punejobs(request):
	return HttpResponse('<h1> Pune Jobs Information </h1>')


def mumbaijobs(request):
	return HttpResponse('<h1> Mumbai Jobs Information </h1>')


def home(req):
	return HttpResponse('Home Page')