from django.conf.urls import patterns, url
from apps.portfolio.views import CategoryList


urlpatterns = patterns(
    'apps.portfolio.views',
    url(r'^$', CategoryList.as_view(), name='portfolio'))