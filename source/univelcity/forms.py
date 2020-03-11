from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')