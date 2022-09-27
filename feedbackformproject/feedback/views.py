from django.shortcuts import render, redirect, HttpResponse
from . import forms 

def feedbackView(request):
    form = forms.FeedbackForm()

    if request.method == 'POST':
        form = forms.FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            roll = form.cleaned_data['rollno']
            email = form.cleaned_data['email']
            feedback = form.cleaned_data['feedback']

            print(name, email, feedback, roll)
            return redirect('home')
    return render(request, 'feedback/feedback.html', context={
        'form': form,
    })


def home(req):
    return HttpResponse('Hello')

def cow(req):
    return HttpResponse('Cow')