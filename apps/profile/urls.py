from django.conf.urls import patterns, url

from apps.profile.views import LoginView, MainView, SignView


urlpatterns = patterns(
    'apps.profile.views',
    url(r'^$', MainView.as_view(), name='main'),
    url(r'^sign', SignView.as_view(), name='sign'),
    url(r'^login/$', LoginView.as_view(), name='login'),)