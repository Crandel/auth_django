from cms.models.pluginmodel import CMSPlugin

from django.db import models
from django.utils.translation import ugettext_lazy as _

class ContactAddress(CMSPlugin):
    """
    Model for getting sitco address details in contact page.
    """
    name = models.CharField(_('Company name'),max_length=255,)
    line1 = models.CharField(_('Addree Line1'),max_length=255,)
    line2 = models.CharField(_('P.O Box'),max_length=100,)
    city = models.CharField(_('City'),max_length=100,)
    country = models.CharField(_('Country name'),max_length=100,)
    tele = models.CharField(_('Telephone number'),max_length=100,)
    fax = models.CharField(_('Fax'),max_length=100,)
    email = models.EmailField(_('Email ID'),max_length=100,)
    web = models.CharField(_('Website'),max_length=100,)
