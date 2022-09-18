from django.shortcuts import render
from datetime import datetime

def home(request):
	date = datetime.now().strftime("%I:%M:%S %p")
	context = {
		'date': date,
	}
	return render(request, 'testApp/test.html', context)
