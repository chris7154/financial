from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User # Import your custom User model

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'is_instructor', 
        'is_student','password1', 'password2']

