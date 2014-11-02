from django.db import models
from django.utils.translation import ugettext_lazy as _

class XMLSitemap(models.Model):
    CHANGE_FREQ_CHOICES = (
    ('always',_('Always')),
    ('hourly',_('hourly')),
    ('daily',_('daily')),
    ('weekly',_('weekly')),
    ('monthly',_('monthly')),
    ('yearly',_('yearly')),
    ('never',_('never')),
    )
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    changefreq = models.CharField(max_length=20,choices=CHANGE_FREQ_CHOICES,default='weekly')

    def __unicode__(self):
        return '%s' %self.title

    class Meta:
        verbose_name = _('Xml Sitemap')
        verbose_name_plural = "Xml Sitemaps"

    @classmethod
    def get_active_siteurls(cls):
        return cls.objects.filter(active=True)