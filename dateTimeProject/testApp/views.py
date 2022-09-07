from django.shortcuts import render, HttpResponse
from datetime import datetime


def greeting(request):
	current_hour = datetime.now().strftime('%H')
	current_hour = int(current_hour)

	if current_hour < 12:
		greeting = 'Morning'
	elif current_hour < 16:
		greeting = 'Afternoon'
	elif current_hour < 21:
		greeting = 'Evening'
	else:
		greeting = 'Night'

	message = f'Hello Imran, Good {greeting}'
	time = f'Current Server time is {datetime.now().strftime("%I:%M:%S %p")}'
	return HttpResponse(f' <h1>{message} <br> {time} </h1>')