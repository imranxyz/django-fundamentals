from django.shortcuts import render
from . import models 

def home(req):
	filters = models.FilterDemo.objects.all()
	return render(request=req, template_name='index.html', context={
			'filters': filters,
		})