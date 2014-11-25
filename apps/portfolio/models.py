from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from autoslug import AutoSlugField
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse


class PortfolioInfo(models.Model):
    """
    Model for managing portfolio
    """
    site = models.ForeignKey(Site, unique=True, null=True)
    title = models.CharField(_('Title'), max_length=255,)
    header_image = models.ImageField(_('Image'), max_length=255, upload_to="portfolio/header/", null=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _('PortfolioInfo')
        verbose_name_plural = _('PortfolioInfo`s')


class Category(models.Model):
    """
    Model for project listing page
    """
    title = models.CharField(_('Title'), max_length=255,)
    slug = AutoSlugField(populate_from='title', unique=True)
    header_image = models.ImageField(_('Image for header'), max_length=255, upload_to="project/header", null=True)
    thumbnail_image = models.ImageField(_('Image for thumbnail'), max_length=255, upload_to="project/thumbnail", null=True)
    order = models.PositiveSmallIntegerField(_('Sort Order'), default=1)

    def get_absolute_url(self):
        return reverse('project_list', kwargs={'category': self.slug})

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

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'project': self.slug, 'category': self.category.slug})


class Image(models.Model):
    project = models.ForeignKey(Project, verbose_name='Project', related_name='images')
    image = models.ImageField(_('Image'), max_length=255, upload_to="project/image")
    title = models.CharField(_('Title'), max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')