from django import forms 
from . import models

class StudentForm(forms.ModelForm):
	class Meta:
		model = models.Student 
		fields = ['name', 'marks']