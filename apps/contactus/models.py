from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site


class ContactUs(models.Model):
    """
    Model for managing contact us page inner section of form.

    """
    site = models.ForeignKey(Site)
    name = models.CharField(_('Name'), max_length=100,)
    company_name = models.CharField(_('Company Name'), max_length=100, null=True)
    email = models.EmailField(_('Email Address'), max_length=100,)
    telephone = models.CharField(_('Telephone'), max_length=100,)
    subject = models.CharField(_('Subject'), null=True, max_length=255)
    details = models.TextField(_('Details'), null=True)
    date = models.DateTimeField(_('Contacted Time'), auto_now=True)

    def __unicode__(self):
        return self.site.name

    class Meta:
        verbose_name = _('Contact Us')
        verbose_name_plural = _('Contact Us')


class GoogleContact(models.Model):
    """
    Model for managing contact us page inner section of form.

    """
    site = models.ForeignKey(Site,unique=True)
    lati = models.CharField(_('Latitude'), max_length=100)
    long = models.CharField(_('Longitude'),max_length=100)


    def __unicode__(self):
        return self.site.name

    class Meta:
        verbose_name = _('Google map setting')
        verbose_name_plural = _('Google map settings')
