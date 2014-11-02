from django.conf.urls import patterns, url
from apps.newsevents.views import EventsView

urlpatterns = patterns('',
    url(r'^events/$', EventsView.as_view(), name='events'))