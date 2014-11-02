from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site

from ckeditor.fields import RichTextField

class Events(models.Model):
    """
    Model for managing Events.

    """
    site = models.ForeignKey(Site)
    event_title = models.CharField(_('Event Title'), max_length=100,)
    event_date_time = models.DateTimeField(_('Event Date and Time'))
    event_desc = RichTextField(_('Event Description'))
    is_published = models.BooleanField(_('Is published'))
    sort_order = models.PositiveSmallIntegerField(_('Sort Order'),default=0)

    def __unicode__(self):
        return self.event_title

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')
        ordering = ['sort_order']


class NewsYear(models.Model):

    news_year = models.CharField(_('News year'), max_length=100,)

    def __unicode__(self):
        return self.news_year

    class Meta:
        ordering = ['-news_year']


class News(models.Model):
    """
    Model for managing News.

    """
    site = models.ForeignKey(Site)
    news_year = models.ForeignKey(NewsYear)
    news_title = models.CharField(_('News Title'), max_length=100,)
    news_date_time = models.DateTimeField(_('News Date and Time'))
    news_desc = RichTextField(_('News Description'))
    news_image = models.ImageField(_('News Image'),upload_to='news/')
    is_published = models.BooleanField(_('Is published'))
    sort_order = models.PositiveSmallIntegerField(_('Sort Order'),default=0)

    def __unicode__(self):
        return self.news_title

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News')
        ordering = ['-sort_order']