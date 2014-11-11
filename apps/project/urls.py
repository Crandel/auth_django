from django.conf.urls import patterns, url
from apps.project.views import RedirectCategory, ProjectListDetail


urlpatterns = patterns(
    'apps.project.views',
    url(r'^$', RedirectCategory.as_view(), name='proj_list_redirect'),
    url(r'^(?P<category>[\w-]+)/$', ProjectListDetail.as_view(), name='proj_list'),)
