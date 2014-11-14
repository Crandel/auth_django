from datetime import date

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site


class FooterSettings(models.Model):
    """
    Model for managing Footer contents.
    """
    site = models.ForeignKey(Site,unique=True)
    copyright = models.CharField(_('Copy Right Text'), max_length=100,)
    twit_url = models.URLField(_('Twitter Url'))
    hide_twi = models.BooleanField(_('Hide twitter icon'), default=False)
    lin_url = models.URLField(_('LinkedIn Url'), null=True)
    hide_lin = models.BooleanField(_('Hide LinkedIn icon'), default=False)

    def __unicode__(self):
        return self.copyright

    class Meta:
        verbose_name = _('Footer Setting')
        verbose_name_plural = _('Footer Settings')



class CommonSettings(models.Model):
    """
    Model for managing common site contents like logo.
    """
    site = models.ForeignKey(Site,unique=True)
    logo_icon = models.ImageField(_('Logo Image'),upload_to='logo/')
    logo_url = models.URLField(_('Logo Url'),null=True,blank=True)

    def __unicode__(self):
        return self.site.name

    class Meta:
        verbose_name = _('Common Setting')
        verbose_name_plural = _('Common Settings')


class AdminEmails(models.Model):
    """
    Model for managing Admin emails for each apps.

    """
    site = models.ForeignKey(Site,unique=True)
    con_email = models.EmailField(_('Contact admin email'), max_length=100)
    career_email = models.EmailField(_('Career admin email'), max_length=100)

    def __unicode__(self):
        return self.site.name

    class Meta:
        verbose_name = _('Admin emails Setting')
        verbose_name_plural = _('Admin emails Settings')


class BannerSettings(models.Model):
    """
    Model for managing banners of each page.
    """
    site = models.ForeignKey(Site,unique=True)
    cont_page = models.ImageField(_('Contact page banner'),upload_to='page_banners/')
    career_page = models.ImageField(_('Career page banner'),upload_to='page_banners/')
    flat_page = models.ImageField(_('Flat page banner'),upload_to='page_banners/')
    news_page = models.ImageField(_('News & Event page banner'),upload_to='page_banners/')
    subsideri_page = models.ImageField(_('Subsidiaries page banner'),upload_to='page_banners/')
    search_page = models.ImageField(_('Search page banner'),upload_to='page_banners/')
    sitemap_page = models.ImageField(_('Sitemap page banner'),upload_to='page_banners/')

    def __unicode__(self):
        return self.site.name

    class Meta:
        verbose_name = _('Page banner management')
        verbose_name_plural = _('Page banner management')


class BannerImages(models.Model):
    """
    Model for managing banner images.
    """
    title = models.CharField(verbose_name=_('Title'), max_length=255)
    image = models.ImageField(verbose_name=_('Image'), upload_to="images/banner/%Y/%m/%d/", max_length=200,)
    link = models.URLField(verbose_name=_('URL'), null=True, blank=True)
    sort_order = models.PositiveSmallIntegerField(_('Sort Order'), default=1)
    published = models.BooleanField(_('Published?'), default=True)

    class Meta:
        verbose_name = _("Banner Image")
        verbose_name_plural = _("Banner Images")
        ordering = ('sort_order', 'title')

    def __unicode__(self):
        return u"%s" % (self.image)

    @classmethod
    def get_published_banners(cls):
        return cls.objects.filter(published=True)

    def admin_thumbnail(self):
        return u'<img src="%s" width= "50" height="50"/>' % (self.image.url)
    admin_thumbnail.short_description = 'Thumbnail'
    admin_thumbnail.allow_tags = True


class TopMenuUrl(models.Model):
    site = models.ForeignKey(Site)
    name = models.CharField(_('Link name'), max_length=255)
    url = models.URLField(_('Url'), max_length=1000)
    sort = models.PositiveSmallIntegerField(_('Order'), default=1)

    class Meta:
        verbose_name = _('Top Menu Url')
        verbose_name_plural = _('Top Menu Urls')
        ordering = ('-sort',)
