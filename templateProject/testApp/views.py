from django.shortcuts import render
from datetime import datetime

def wish(request):
	context = {
		'Hello': 'Imran',
		'date': datetime.now().strftime('%I:%M:%S %p')
	}
	return render(request, 'testApp/index.html', context=context)