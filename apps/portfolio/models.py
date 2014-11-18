from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from autoslug import AutoSlugField


class PortfolioInfo(models.Model):
    """
    Model for managing portfolio
    """
    title = models.CharField(_('Title'), max_length=255,)
    header_image = models.ImageField(_('Image'), max_length=255, upload_to="portfolio/header/", null=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _('Portfolio')
        verbose_name_plural = _('Portfolio')


class Category(models.Model):
    """
    Model for project listing page
    """
    title = models.CharField(_('Title'), max_length=255,)
    slug = AutoSlugField(populate_from='title', unique=True)
    header_image = models.ImageField(_('Image'), max_length=255, upload_to="project/header", null=True)
    thumbnail_image = models.ImageField(_('Image'), max_length=255, upload_to="project/thumbnail", null=True)
    order = models.PositiveSmallIntegerField(_('Sort Order'), default=1)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ('order',)


class Project(models.Model):
    """
    Model for project detail page
    """
    category = models.ForeignKey(Category, verbose_name='Category', related_name='projects')
    title = models.CharField(_('Title'), max_length=255)
    slug = AutoSlugField(populate_from='title', unique=True)
    client = models.CharField(_('Client'), max_length=255)
    location = models.CharField(_('Location'), max_length=255)
    scope = models.CharField(_('Scope'), max_length=255)
    description = models.CharField(_('Description'), max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')


class Image(models.Model):
    project = models.ForeignKey(Project, verbose_name='Project', related_name='images')
    image = models.ImageField(_('Image'), max_length=255, upload_to="project/image")
    title = models.CharField(_('Title'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')

