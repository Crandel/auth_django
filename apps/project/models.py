from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from autoslug import AutoSlugField


class Category(models.Model):
    name = models.CharField(_('Name'), max_length=255)
    slug = AutoSlugField(populate_from='name', unique=True)
    order = models.PositiveSmallIntegerField(_('Ordering'), default=1)

    class Meta:
        verbose_name = _('Ctegory')
        verbose_name_plural = _('Categories')
        ordering = ('order',)


class Project(models.Model):

    project = models.CharField(_('Project'), max_length=255)
    slug = AutoSlugField(populate_from='project', unique=True)
    category = models.ForeignKey(Category, verbose_name=_('category'), related_name='projects')
    client = models.CharField(_('Client'), max_length=255)
    location = models.CharField(_('Location'), max_length=255)
    scope = models.CharField(_('Scope'), max_length=1000)
    description = models.TextField(_('Description'))
    publish = models.BooleanField(_('Publish'), default=True)

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')


class Image(models.Model):

    project = models.ForeignKey(Project, verbose_name=_('Project'), related_name='images')
    title = models.CharField(_('Title'), max_length=255, blank=True, null=True)
    image = models.ImageField(_('Image'), upload_to='project/', max_length=255)
    publish = models.BooleanField(_('Publish'), default=True)

    class Meta:
        verbose_name = _('Project Image')
        verbose_name_plural = _('Project Images')
