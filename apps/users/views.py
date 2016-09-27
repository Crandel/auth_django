import hashlib
from datetime import datetime

from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, FormView, CreateView, View, UpdateView
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.http import HttpResponse, Http404

from .forms import LoginForm, UserForm, ProfileForm

User = get_user_model()


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if not user:
            raise Http404
        else:
            login(self.request, user)
        return super(LoginView, self).form_valid(form)


class SuccessView(View):

    def get(self, *args, **kwargs):
        return HttpResponse('Thank you for signing, please activate your email')


class LogoutView(View):

    def get(self, *args, **kwargs):
        logout(self.request)
        return redirect(reverse('login'))


class ActivateView(View):

    def get(self, *args, **kwargs):
        # hashing = self.kwargs.get('key', None)
        # profile = Profile.objects.get(authentication_hash=hashing)
        # if not profile.user:
        #     raise Http404
        # profile.user.is_active = True
        # profile.user.save()
        # profile.user.backend = 'django.contrib.auth.backends.ModelBackend'
        # login(self.request, profile.user)
        return redirect(reverse('main'))


class MainView(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        user = self.request.user
        if not user.is_authenticated():
            return redirect(reverse('login'))
        context['user'] = user
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        user = request.user
        if not user.is_authenticated():
            return redirect(reverse('login'))
        return context


class SignView(CreateView):
    template_name = 'sign.html'
    form_class = UserForm
    success_url = '/success'

    def get_context_data(self, **kwargs):
        context = super(SignView, self).get_context_data(**kwargs)
        context['profile'] = kwargs['profile'] if 'profile' in kwargs else ProfileForm
        return context

    def post(self, request, *args, **kwargs):

        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            user = form.save(commit=False)
            password = user.password
            hashing = hashlib.sha224(str(datetime.now())).hexdigest()

            user.is_active = False
            user.set_password(password)

            profile_form = ProfileForm(request.POST, request.FILES)

            if not profile_form.is_valid():
                return self.render_to_response(self.get_context_data(profile=profile_form, form=form))

            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.authentication_hash = hashing

            profile.save()
            url = self.request.META['HTTP_HOST'] + profile.get_absolute_url()

            html = render_to_string('email.html', {'user': user, 'password': password, 'url': url})

            send_mail('Confirm email', html, 'vitaliy@steelkiwi.com', [user.email])
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class ChangeUserView(UpdateView):
    model = User
    fields = ['username', 'email', 'first_name', 'last_name']
    template_name = 'change/change_user.html'

    def form_valid(self, form):
        user = form.save()
        return redirect(reverse('change_profile', kwargs={'pk': user.id}))


class ChangeProfileView(UpdateView):
    model = User
    fields = ['phone', 'address', 'profile_photo']
    template_name = 'change/change_profile.html'
