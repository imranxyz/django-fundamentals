from django.urls import path
from . import views

urlpatterns = [
	path('wish/', views.wish, name='wish'),
]