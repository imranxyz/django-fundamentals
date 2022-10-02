from django.urls import path 
from . import views

urlpatterns = [
	path('register/', views.StudentView, name='register')
]