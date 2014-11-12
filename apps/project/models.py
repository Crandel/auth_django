from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site
from autoslug import AutoSlugField


class PortfolioInfo(models.Model):
    """
    Model for managing career vaccancy listing.

    """
    site = models.ForeignKey(Site, unique=True)
    title = models.CharField(_('Title'), max_length=255,)
    image = models.ImageField(_('Image'), max_length=255, upload_to="project/", null=True)

    def __unicode__(self):
        return "Portfolio information for %s" % self.site.name

    class Meta:
        verbose_name = _('Portfolio Information')
        verbose_name_plural = _('Portfolio Informations')


class Category(models.Model):
    name = models.CharField(_('Name'), max_length=255)
    slug = AutoSlugField(populate_from='name', unique=True)
    image = models.ImageField(_('Image'), upload_to='category/', max_length=255, null=True)
    order = models.PositiveSmallIntegerField(_('Ordering'), default=1)

    class Meta:
        verbose_name = _('Ctegory')
        verbose_name_plural = _('Categories')
        ordering = ('order',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('proj_list', kwargs={'category': self.slug})

    def admin_thumbnail(self):
        return u'<img src="%s" width= "50" height="50"/>' % (self.image.url)
    admin_thumbnail.short_description = 'Thumbnail'
    admin_thumbnail.allow_tags = True


class Project(models.Model):

    project = models.CharField(_('Project'), max_length=255)
    slug = AutoSlugField(populate_from='project', unique=True)
    short_name = models.CharField(_('Short name'), max_length=255, null=True)
    category = models.ForeignKey(Category, verbose_name=_('category'), related_name='projects')
    client = models.CharField(_('Client'), max_length=255)
    location = models.CharField(_('Location'), max_length=255)
    scope = models.CharField(_('Scope'), max_length=1000)
    description = models.TextField(_('Description'))
    publish = models.BooleanField(_('Publish'), default=True)

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')

    def __str__(self):
        return self.project

    def get_absolute_url(self):
        return reverse('proj_detail', kwargs={'category': self.category.slug, 'slug': self.slug})


class Image(models.Model):

    project = models.ForeignKey(Project, verbose_name=_('Project'), related_name='images')
    title = models.CharField(_('Title'), max_length=255, null=True)
    image = models.ImageField(verbose_name=_('Image'), upload_to='project/', max_length=255)
    order = models.BooleanField(_('Order'), default=1)

    class Meta:
        verbose_name = _('Project Image')
        verbose_name_plural = _('Project Images')
        ordering = ('order',)

    def __str__(self):
        return self.title
