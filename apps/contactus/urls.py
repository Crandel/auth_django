from django.conf.urls import patterns, url
from apps.contactus.views import ContactView


urlpatterns = patterns('',
    url(r'^$', ContactView.as_view(), name='contactus'))