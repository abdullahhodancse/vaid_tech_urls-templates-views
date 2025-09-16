from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class UserRegistrationForm(UserCreationForm):


    first_name=forms.CharField(required=True)
    last_name=forms.CharField(required=True)
    roll=forms.IntegerField(required=True)
    department=forms.CharField(required=True)
    reg=forms.IntegerField(required=True)
    session=forms.CharField(required=True)
    email=forms.CharField(required=True)


    class Meta:
        model = User
        fields=['username','first_name','last_name','email','roll','reg','department','session','password1','password2']

   
