from __future__ import unicode_literals

from django.db import models
from django.contrib.sites.models import Site
from django.core.urlresolvers import get_script_prefix
from django.utils.translation import ugettext_lazy as _

from cms.models.pluginmodel import CMSPlugin
from ckeditor.fields import RichTextField


class FlatPage(models.Model):
    url = models.CharField(_('URL'), max_length=100, db_index=True)
    title = models.CharField(_('title'), max_length=200)
    content = models.TextField(_('content'), blank=True)
    enable_comments = models.BooleanField(_('enable comments'), default=False)
    template_name = models.CharField(_('template name'), max_length=70, blank=True,
        help_text=_("Example: 'flatpages/contact_page.html'. If this isn't provided, the system will use 'flatpages/default.html'."))
    registration_required = models.BooleanField(_('registration required'),
        help_text=_("If this is checked, only logged-in users will be able to view the page."),
        default=False)
    sites = models.ManyToManyField(Site)
    FLATPAGE_CHOICES = (
        ('about', 'About Us'),
        ('footer', 'Footer Pages'),
    )
    select_link = models.CharField(_('Select where to deploy the page'),max_length=50,
                                      choices=FLATPAGE_CHOICES,
                                      default='about')
    sort_order = models.PositiveSmallIntegerField(_('Sort Order'),default=0)
    class Meta:
        db_table = 'django_flatpage'
        verbose_name = _('flat page')
        verbose_name_plural = _('flat pages')
        ordering = ('sort_order',)

    def __str__(self):
        return "%s -- %s" % (self.url, self.title)

    def get_absolute_url(self):
        # Handle script prefix manually because we bypass reverse()
        return iri_to_uri(get_script_prefix().rstrip('/') + self.url)


class HomeFlatPagePluginModel(CMSPlugin):
    """
      Model for about-us page plugin
    """
    title = models.CharField(_('Title'), max_length=250, null=True, blank=True)
    details = RichTextField(_('Details'))
    is_signature = models.BooleanField(_('Signature'), default=False)
    signature_image = models.ImageField(_('Signature Image'), upload_to='signature_image/', blank=True)
    chairman = models.CharField(_('Chairman'), max_length=255, blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _('About')
        verbose_name_plural = _('About')
