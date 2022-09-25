from django.shortcuts import render
from . import models


def hydjobs(request):
	emp_list = models.Hydjobs.objects.all()

	return render(request, 'jobApp/hydjobs.html', context={
		'employees': emp_list,
		})

def kolkatajobs(request):
	emp_list = models.Hydjobs.objects.all()

	return render(request, 'jobApp/kolkatajobs.html', context={
		'employees': emp_list,
		})

def punejobs(request):
	emp_list = models.Hydjobs.objects.all()

	return render(request, 'jobApp/index.html', context={
		'employees': emp_list,
		})

def banglorejobs(request):
	emp_list = models.Hydjobs.objects.all()

	return render(request, 'jobApp/banglorejobs.html', context={
		'employees': emp_list,
		})