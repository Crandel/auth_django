from django.conf.urls import patterns, url
from apps.home.views import HomePageView


urlpatterns = patterns('',
    url(r'^$', HomePageView.as_view(), name='contactus'))