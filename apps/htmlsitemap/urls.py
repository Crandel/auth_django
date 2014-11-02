from django.conf.urls import patterns, url
from apps.htmlsitemap.views import Sitemapiew

urlpatterns = patterns('',
    url(r'^site_map/$', Sitemapiew.as_view(), name='sitemap'))