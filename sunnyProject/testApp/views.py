from django.shortcuts import render

def home(request):
	return render(request, 'testApp/home.html', context= {
		'home': 'Home',
		})


def profile(request):
	return render(request, 'testApp/profile.html', context = {
		'profile': 'Profile'
		})