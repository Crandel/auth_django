from django.views.generic import TemplateView, View


class LoginView(TemplateView):
    template_name = 'login.html'

    # def get(self, request, *args, **kwargs):
    #     context = True


class MainView(TemplateView):
    template_name = 'main.html'


class SignView(TemplateView):
    template_name = 'sign/first_page.html'