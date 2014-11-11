from django.conf.urls import patterns, url
from apps.project.views import PortfolioPage, ProjectListDetail, ProjectDetail, LoadMoreProject, LoadMoreCategory


urlpatterns = patterns(
    'apps.project.views',
    url(r'^$', PortfolioPage.as_view(), name='portfolio_page'),
    url(r'^more/$', LoadMoreCategory.as_view(), name='load_more_cat'),
    url(r'^more/(?P<category>[\w-]+)/$', LoadMoreProject.as_view(), name='load_more_proj'),
    url(r'^(?P<category>[\w-]+)/$', ProjectListDetail.as_view(), name='proj_list'),
    url(r'^(?P<category>[\w-]+)/(?P<slug>[\w-]+)/$', ProjectDetail.as_view(), name='proj_detail'),)
