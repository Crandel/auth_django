from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Portfolio(models.Model):
    """
    Model for managing portfolio
    """
    title = models.CharField(_('Title'), max_length=255,)
    header_image = models.ImageField(_('Image'), max_length=255, upload_to="portfolio/header/", null=True)
    project_listing_page = models.ForeignKey(ProjectListingPage, verbose_name=_('Project Listing Page'))


class ProjectListingPage(models.Model):
    """
    Model for project listing page
    """
    title = models.CharField(_('Title'), max_length=255,)
    header_image = models.ImageField(_('Image'), max_length=255, upload_to="portfolio/header", null=True)
    thumbnail_image = models.ImageField(_('Image'), max_length=255, upload_to="portfolio/thumbnail", null=True)
    project_detail_page = models.ForeignKey(ProjectDetailPage, verbose_name=_('Project Detail Page'))


class ProjectDetailPage(models.Model):
    """
    Model for project detail page
    """
    title = models.CharField(_('Title'), max_length=255)
    project = models.CharField(_('Project'), max_length=255)
    client = models.CharField(_('Client'), max_length=255)
    location = models.CharField(_('Location'), max_length=255)
    scope = models.CharField(_('Scope'), max_length=255)
    description = models.CharField(_('Description'), max_length=255)
