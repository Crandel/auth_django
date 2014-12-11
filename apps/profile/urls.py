from django.conf.urls import patterns, url

from apps.profile.views import LoginView, MainView, SignView, ActivateView, LogoutView, SuccessView, ChangeView


urlpatterns = patterns(
    'apps.profile.views',
    url(r'^$', MainView.as_view(), name='main'),
    url(r'^sign/$', SignView.as_view(), name='sign'),
    url(r'^activate/(?P<key>[\w-]+)/$', ActivateView.as_view(), name='activate'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^success/$', SuccessView.as_view(), name='success'),
    url(r'^change/$', ChangeView.as_view(), name='change'),)