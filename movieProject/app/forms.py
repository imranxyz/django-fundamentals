from django import forms
from . import models

class MovieForm(forms.ModelForm):
	# date = forms.DateField(label='Release Date')
	class Meta:
		model = models.Movie
		fields = ['date', 'name', 'hero', 'heroine', 'rating']