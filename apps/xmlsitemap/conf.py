from django.conf import settings

#Example in your settings.py file
#from ***.sitemaps import TagSitemap,EntrySitemap
#from cms.sitemaps import CMSSitemap
#XML_OTHER_SITEMAPS = {
#'blog':EntrySitemap,
#'blog_tags':TagSitemap,
#'cms_tags':CMSSitemap, # for cms sitemap
#}
OTHER_SITEMAPS = getattr(settings,'XML_OTHER_SITEMAPS',{})