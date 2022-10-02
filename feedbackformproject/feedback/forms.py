from django import forms 
from django.core import validators

# custom validation with built in method
def NameValidation(name):
    if not name[0].lower() == 'd':
        raise forms.ValidationError('Name Must be starts with D')

def only_gmail(email):
    if not email.endswith('gmail.com'):
        raise forms.ValidationError('Only Gmail is accepted')


class FeedbackForm(forms.Form):
    name = forms.CharField(label='Full Name', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'name',
    }), validators=[NameValidation])
    rollno = forms.IntegerField(label='Roll', widget=forms.TextInput(attrs={
        'id': 'roll',
        'class': 'form-control',
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }), validators=[only_gmail])
    feedback = forms.CharField(validators=[validators.MaxLengthValidator(40), validators.MinLengthValidator(10)],widget=forms.Textarea(attrs={
        'class': 'form-control',
    }))
    password = forms.CharField(widget=forms.PasswordInput)
    rpassword = forms.CharField(widget=forms.PasswordInput(attrs={
            'name': 'password-again'
        }), label='Password(again)')

    # single custom validation 
    # def clean_name(self):
    #     input = self.cleaned_data['name']

    #     if len(input) < 4:
    #         raise forms.ValidationError('Name must be 4+ Characters')
    
    #     return input
    
    # def clean_rollno(self):
    #     input = self.cleaned_data['rollno']

    #     if not isinstance(input, int) or len(str(input)) < 3:
    #         raise forms.ValidationError('Roll must be integers with 8 characters')

    # custom validation under single function
    def clean(self):
        print('total form validation')
        cleaned_data = super().clean()

        inputName = cleaned_data['name']
        if len(inputName) < 5:
            raise forms.ValidationError('Name must be 5+ Character')

        inputRoll = self.cleaned_data['rollno']
        if not isinstance(inputRoll, int) or len(str(input)) < 3:
            raise forms.ValidationError('Roll must be integers with 8 characters')

        password = self.cleaned_data['password']
        rpassword = self.cleaned_data['rpassword']
        if password != rpassword:
            raise forms.ValidationError('Not Matched,try again')