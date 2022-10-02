from django.shortcuts import render
from . import forms

def StudentView(request):
	form = forms.StudentForm()

	if request.method == 'POST':
		form = forms.StudentForm(request.POST)
		if form.is_valid():
			form.save()
			form = forms.StudentForm()

	return render(request, 'testApp/register.html', context={'form': form})