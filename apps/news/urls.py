from django.conf.urls import patterns, url
from apps.news.views import NewsView, LoadMoreNews

urlpatterns = patterns(
    'apps.news.views',
    url(r'^$', NewsView.as_view(), name='news'),
    url(r'^get-more/$', LoadMoreNews.as_view(), name='load_more_news'),
    url(r'^(?P<year>\d+)$', NewsView.as_view(), name='news_by_year'))
