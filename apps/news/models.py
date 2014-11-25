from __future__ import unicode_literals

from datetime import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _


class New(models.Model):
    title = models.CharField(_('Title'), max_length=100,)
    description = models.TextField()
    date = models.DateField(_('Last Date'), auto_now_add=True, blank=True)
    year = models.IntegerField(_('Year'), default=datetime.now().year)
    image = models.ImageField(_('Image'), max_length=255, upload_to="news/image", null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('New')
        verbose_name_plural = _('News')
        ordering = ('year',)