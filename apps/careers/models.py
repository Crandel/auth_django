from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site
from ckeditor.fields import RichTextField
from model_utils.models import TimeStampedModel


class CareerInfo(models.Model):
    """
    Model for managing career vaccancy listing.

    """
    site = models.ForeignKey(Site, unique=True)
    title = models.CharField(_('Title'), max_length=255,)
    image = models.ImageField(_('Image'), max_length=255, upload_to="careers/", null=True)
    description = RichTextField()

    def __unicode__(self):
        return "Career information for %s" % self.site.name

    class Meta:
        verbose_name = _('Career Information')
        verbose_name_plural = _('Career Informations')


class SVModel(TimeStampedModel):
    cv = models.FileField(_('Resume'), upload_to='resume/', max_length=1000)

    class Meta:
        verbose_name = _('Resume')
        verbose_name = _('Resumes')
        ordering = ('created',)


class Vacancy(TimeStampedModel):
    site = models.ForeignKey(Site, verbose_name=_('Site'))
    position = models.CharField(_('Job Position'), max_length=1000)
    requirement = RichTextField(_('Requirement'))
    last_date = models.DateField(_('Last Date'), default=datetime.datetime.now())
    is_published = models.BooleanField(_('Is Published'), default=True)
    sort = models.PositiveSmallIntegerField(_('Sort Order'), default=1)

    class Meta:
        verbose_name = _('Vacancy')
        verbose_name_plural = _('Vacancies')
        ordering = ('sort', '-created')

    def __str__(self):
        return self.position


class JobCategory(models.Model):
    """
    Model for managing Job categories listing.
    """
    catog = models.CharField(_('Job Category'), max_length=255,)
    sort_order = models.PositiveSmallIntegerField(_('Sort Order'),default=0)

    def __unicode__(self):
        return self.catog

    class Meta:
        verbose_name = _('Job Category')
        verbose_name_plural = _('Job Categories')
        ordering = ('sort_order',)

class Career(models.Model):
    """
    Model for managing career vaccancy listing.

    """
    site = models.ForeignKey(Site)
    job_cat = models.ForeignKey(JobCategory,verbose_name=_('Job Category'))
    designation = models.CharField(_('Designation'), max_length=255,)
    short_desc = RichTextField(_('Short Description'))
    date = models.DateTimeField(_('Created Date/Time'))
    cl_time = models.DateTimeField(_('Closing Date/Time'))
    is_published = models.BooleanField(_('Is Published'))
    sort_order = models.PositiveSmallIntegerField(_('Sort Order'),default=0)

    def __unicode__(self):
        return "%s vaccancy from %s" %(self.designation,self.site.name)

    class Meta:
        verbose_name = _('Job vacancy')
        verbose_name_plural = _('Job vacancies')
        ordering = ('-sort_order',)



class AppliedJobs(models.Model):
    """
    Model for managing Applied jobs.

    """
    site = models.ForeignKey(Site)
    designation = models.CharField(_('Designation'), max_length=255,)
    job_cat = models.ForeignKey(JobCategory,verbose_name=_('Job Category'),null=True,blank=True)
    name = models.CharField(_('Name of Applicant'), max_length=255,)
    email = models.EmailField(_('Email Address'), max_length=255,)
    tele = models.CharField(_('Telephone'), max_length=100,)
    upload_file = models.FileField(_('Uploaded CV'),upload_to='upload_cvs/')
    date = models.DateTimeField(_('Applied date'))

    def __unicode__(self):
        return self.designation

    class Meta:
        verbose_name = _('Applied Jobs')
        verbose_name_plural = _('Applied Jobs')

    def upload_file_link(self):
        if self.upload_file:
            return "<a href='%s'>download cv</a>" % (self.upload_file.url,)
        else:
            return "No attachment"

    upload_file_link.allow_tags = True

