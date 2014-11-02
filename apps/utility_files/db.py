from django.db import models
from django.utils.translation import ugettext_lazy as _

from django_extensions.db.fields import (ModificationDateTimeField,
                                        CreationDateTimeField, AutoSlugField)


class BaseModel(models.Model):
    """
    Base model that provides:
        * title
        * self managed slug
        * self managed created field
        * self managed modified field
    """
    title = models.CharField(_('Title'), max_length=200)
    slug = AutoSlugField(_('Slug'), populate_from='title')
    created = CreationDateTimeField(_('Created'))
    modified = ModificationDateTimeField(_('Modified'))

    class Meta:
        get_latest_by = 'modified'
        ordering = ('-modified', '-created',)
        abstract = True

class DateBaseModel(models.Model):
    """
    Base model that provides:
        * self managed created field
        * self managed modified field
    """
    created = CreationDateTimeField(_('created'))
    modified = ModificationDateTimeField(_('modified'))

    class Meta:
        get_latest_by = 'modified'
        ordering = ('-modified', '-created',)
        abstract = True


