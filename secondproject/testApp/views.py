from django.shortcuts import render, HttpResponse
from datetime import datetime

def TimeInfo(request):
	date = datetime.now()
	message = '<h1>Hello, Friend Good Noon!!</h1>'
	message += f'<h1>Server time is {date} </h1>'

	return HttpResponse(message)