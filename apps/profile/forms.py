from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from apps.profile.models import Profile


class LoginForm(AuthenticationForm):
    pass


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['phone', 'address', 'profile_photo']
