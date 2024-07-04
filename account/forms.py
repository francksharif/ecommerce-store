from typing import Any
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.models import User
from django import forms



""" User Login Form """

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())







""" User Registration Form """ 

class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    
    def __init__(self, *args, **kwargs) :
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True

    
    def clean_email(self):
        """ Email validation function """
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email already exists')
        
        if len(email) >= 350:
            raise forms.ValidationError('Your email is not valid')
        
        return email
    


""" User Registration Form """ 

class UpdateUserForm(forms.ModelForm):
    password = None 

    class Meta:
        model = User
        fields = ['username', 'email']
        exclude = ['password1', 'password2']

    def __init__(self, *args, **kwargs) :
        super(UpdateUserForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True