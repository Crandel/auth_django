from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
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

    def cv_file_link(self):
        if self.cv:
            return "<a href='%s'>download cv</a>" % (self.cv.url,)
        else:
            return "No attachment"

    cv_file_link.allow_tags = True


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

    def get_absolute_url(self):
        return reverse('vacancy_apply', kwargs={'pk': self.pk})


class Nationality(models.Model):

    nationality = models.CharField(_('Nationality'), max_length=1000)

    class Meta:
        verbose_name = _('Nationality')
        verbose_name_plural = _('Nationality')
        ordering = ('nationality',)

    def __str__(self):
        return self.nationality


class VacancyApply(TimeStampedModel):
    site = models.ForeignKey(Site, verbose_name=_('Site'))
    vacancy = models.ForeignKey(Vacancy, verbose_name=_('Vacancy'))
    position = models.CharField(_('Position Applied For'), max_length=1000)
    name = models.CharField(_('Name'), max_length=1000)
    nationality = models.ForeignKey(Nationality, verbose_name=_('Nationality'))
    address = models.TextField(_('Present Address'))
    phone = models.CharField(_('Telephone Number'), max_length=16)
    email = models.EmailField(_('Email'), max_length=255)
    cv = models.FileField(_('CV'), upload_to='resume/', max_length=255)

    class Meta:
        verbose_name = _('Vacancy Apply')
        verbose_name_plural = _('Vacancies Apply')
        ordering = ('-created',)

    def __str__(self):
        return "{0} - {1}".format(self.created, self.position)

    def cv_file_link(self):
        if self.cv:
            return "<a href='%s'>download cv</a>" % (self.cv.url,)
        else:
            return "No attachment"

    cv_file_link.allow_tags = True
