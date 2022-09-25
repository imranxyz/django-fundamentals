from django.urls import path 
from . import views 

urlpatterns = [
	path('hydjobs/', views.hydjobs, name='hyd'),
	path('banglorejobs/', views.hydjobs, name='banglore'),
	path('punejobs/', views.hydjobs, name='pune'),
	path('kolkatajobs/', views.hydjobs, name='kolkata'),
]