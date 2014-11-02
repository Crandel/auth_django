from django.contrib import admin
from models import XMLSitemap


class XMLSitemapAdmin(admin.ModelAdmin):
    list_display = ('title','url')
admin.site.register(XMLSitemap,XMLSitemapAdmin)