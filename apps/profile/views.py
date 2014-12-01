from django.views.generic import TemplateView, FormView, CreateView
from django.contrib.auth.models import User

from apps.profile.forms import LoginForm, ProfileForm
from apps.profile.models import Profile


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'


class MainView(TemplateView):
    template_name = 'main.html'


class SignView(CreateView):
    template_name = 'sign.html'
    form_class = ProfileForm
    success_url = '/'

    def form_valid(self, form):
        user = form.save(commit=False)
        password = User.objects.make_random_password()
        user.set_password(password)
        user.save()
        Profile.objects.create(user=user)
        user.email_user('subject', 'message')
        return super(SignView, self).form_valid(form)