from django.conf.urls import patterns, url
from apps.project.views import RedirectCategory, ProjectListDetail, ProjectDetail, LoadMoreProject


urlpatterns = patterns(
    'apps.project.views',
    url(r'^$', RedirectCategory.as_view(), name='proj_list_redirect'),
    url(r'^more/(?P<category>[\w-]+)/$', LoadMoreProject.as_view(), name='load_more_proj'),
    url(r'^(?P<category>[\w-]+)/$', ProjectListDetail.as_view(), name='proj_list'),
    url(r'^(?P<category>[\w-]+)/(?P<slug>[\w-]+)/$', ProjectDetail.as_view(), name='proj_detail'),)
