from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse
#from apps.projects.models import Projects
#from apps.media.models import LatestNews,Videos,PicasoGallery
from apps.xmlsitemap.models import XMLSitemap
#from apps.partner.models import Partner
#from apps.contact.models import Contact
#from portail_portfolio.models import Entry

from datetime import datetime

class BasicSitemap(Sitemap):

    def __init__(self, names):
        self.names = names

    def items(self):
        return self.names

    def changefreq(self, obj):
        return 'weekly'

    def lastmod(self, obj):
        return datetime.now()

    def location(self,obj):
        return reverse(obj)

class ModelSitemap(Sitemap):

#    def __init__(self, names):
#        self.names = names

    def items(self):
        return XMLSitemap.objects.filter(active=True)

    def changefreq(self, obj):
        return obj.changefreq

    def lastmod(self, obj):
        return datetime.now()

    def location(self,obj):
        return obj.url






    




    