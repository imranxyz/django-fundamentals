from django.shortcuts import render
from . import models, forms

# Create your views here.
def StudentView(request):
    form = forms.StudentRegistrationForm()

    # if request.method == 'POST':
    #     form = forms.StudentRegistrationForm(request.POST)
    #     if form.is_valid():
    #         form.save(commit=True)
    #         return redirect('home')

    return render(request, 'testApp/register.html', context={
        'form': form,
    })


def HomeView(request):
    return render(request, 'testApp/home.html')