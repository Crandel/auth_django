from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site
from ckeditor.fields import RichTextField


class NewsInfo(models.Model):
    """
    Model for managing career vaccancy listing.

    """
    site = models.ForeignKey(Site, unique=True, related_name='news_info')
    title = models.CharField(_('Title'), max_length=255,)
    image = models.ImageField(_('Image'), max_length=255, upload_to="careers/", null=True)
    description = RichTextField(_('description'), blank=True)

    def __unicode__(self):
        return "News information for %s" % self.site.name

    class Meta:
        verbose_name = _('News Information')
        verbose_name_plural = _('News Informations')


class News(models.Model):
    """
    Model for managing News.

    """
    site = models.ForeignKey(Site, related_name='news_list')
    title = models.CharField(_('News Title'), max_length=100,)
    date_time = models.DateTimeField(_('News Date and Time'))
    description = RichTextField(_('News Description'))
    image = models.ImageField(_('News Image'), upload_to='news/', blank=True)
    is_published = models.BooleanField(_('Is published'), default=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News')
        ordering = ['-date_time']
