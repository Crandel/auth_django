from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginForm(AuthenticationForm):
    pass


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']


class ProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['phone', 'address', 'avatar']
