from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    login = forms.CharField()
    password = forms.CharField()


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def send_email(self):
        pass