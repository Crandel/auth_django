from django.conf.urls import patterns, url

from apps.portfolio.views import CategoryList, LoadMore, ProjectList, LoadMoreProj, ProjectDetail


urlpatterns = patterns(
    'apps.portfolio.views',
    url(r'^$', CategoryList.as_view(), name='portfolio'),
    url(r'^load_more_cat/$', LoadMore.as_view(), name='load_more_cat'),
    url(r'^load_more_proj/$', LoadMoreProj.as_view(), name='load_more_proj'),
    url(r'^(?P<category>[\w-]+)/$', ProjectList.as_view(), name='project_list'),
    url(r'^(?P<category>[\w-]+)/(?P<project>[\w-]+)/$', ProjectDetail.as_view(), name='project_detail'),
    )
