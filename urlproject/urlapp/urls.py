from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('hydjobs/', views.hydjobs, name='hyd'),
	path('chennaijobs/', views.chennaijobs, name='chennai'),
	path('kolkatajobs/', views.kolkatajobs, name='kolkata'),
	path('punejobs/', views.punejobs, name='pune'),
	path('mumbaijobs/', views.mumbaijobs, name='mumbai'),
]