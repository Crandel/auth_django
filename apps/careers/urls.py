from django.conf.urls import patterns, url
from apps.careers.views import CareerView

urlpatterns = patterns('',
    url(r'^job-vacancies/$', CareerView.as_view(), name='career'))