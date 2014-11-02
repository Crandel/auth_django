from django.conf.urls import patterns,url

from apps.xmlsitemap.conf import OTHER_SITEMAPS
from apps.xmlsitemap.models import XMLSitemap
from apps.xmlsitemap.sitemap import ModelSitemap
#MediaSiteMap,VideoSiteMap,PartnerSiteMap,ContactSitemap

modelsitemaps = {
'page1' : ModelSitemap,
#'page2' :MediaSiteMap,
#'page3':VideoSiteMap,
#'page4':PartnerSiteMap,
#'page5':ContactSitemap,
}
#modelsitemaps.update(OTHER_SITEMAPS)

urlpatterns = patterns('django.contrib.sitemaps.views',
    (r'^sitemap\.xml$', 'sitemap', {'sitemaps': modelsitemaps}),
)