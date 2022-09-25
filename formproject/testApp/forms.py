from django import forms 
from . import models 


class StudentRegistrationForm(forms.Form):
    name = forms.CharField()
    marks = forms.IntegerField()