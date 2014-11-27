from django.conf.urls import patterns, url

from apps.news.views import NewsList, LoadMore


urlpatterns = patterns(
    'apps.news.views',
    url(r'^$', NewsList.as_view(), name='news'),
    url(r'^(?P<year>\d{4})/$', NewsList.as_view(), name='news_year'),
    url(r'^load_more_news/$', LoadMore.as_view(), name='load_more_news'),)