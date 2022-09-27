from django.urls import path 
from . import views

UrlappConfig = [
    path('')
    path('', views.feedbackView, name='feedback')
]