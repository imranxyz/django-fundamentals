from django import forms 


class FeedbackForm(forms.Form):
    name = forms.CharField(label='Full Name', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'name',
    }))
    rollno = forms.IntegerField(label='Roll', widget=forms.TextInput(attrs={
        'id': 'roll',
        'class': 'form-control',
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    feedback = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
    }))