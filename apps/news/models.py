from __future__ import unicode_literals

from datetime import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _


class NewsModel(models.Model):
    title = models.CharField(_('Title'), max_length=100,)
    description = models.TextField(_('Description'), max_length=512)
    date = models.DateField(_('Last Date'), max_length=255, auto_now_add=True)
    year = models.IntegerField(_('Year'), max_length=255, default=datetime.now().year)
    image = models.ImageField(_('Image'), max_length=255, upload_to="news/image", null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('All News')