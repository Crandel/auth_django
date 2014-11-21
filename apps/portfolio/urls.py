from django.conf.urls import patterns, url
from apps.portfolio.views import CategoryList, LoadMore


urlpatterns = patterns(
    'apps.portfolio.views',
    url(r'^$', CategoryList.as_view(), name='portfolio'),
    url(r'^load_more/$', LoadMore.as_view(), name='load_more_cat'),
)