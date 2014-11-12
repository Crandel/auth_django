import datetime

from django.contrib import admin
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from import_export.admin import ExportMixin
from import_export.formats import base_formats
from modeltranslation.admin import TranslationAdmin
from import_export import resources

from apps.careers.models import JobCategory, Career, AppliedJobs, CareerInfo, SVModel, Vacancy
from forms import CareerAdminForm

DEFAULT_FORMATS = (
base_formats.CSV,
base_formats.XLS,
base_formats.TSV,
base_formats.ODS,
base_formats.JSON,
base_formats.YAML,
)

class Jobstatus(admin.SimpleListFilter):
    title = _('Expired Jobs')
    parameter_name = 'expired_jobs'

    def lookups(self, request, model_admin):
        """
        Look up strings on right side of custom filter.
        """
        return (
            ('expired', _('Expired Jobs')),
            ('non_expired', _('Applicable Jobs')),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        if self.value() == 'expired':
            return queryset.filter(cl_time__lte=datetime.datetime.now())
        if self.value() == 'non_expired':
            return queryset.filter(cl_time__gte=datetime.datetime.now())



class CareerAdmin(TranslationAdmin):
    """
    Career admin to view manage career vaccancy.
    """
    form = CareerAdminForm
    model=Career
    list_display = ['designation','is_published','sort_order']
    list_filter = ['job_cat','is_published',Jobstatus,'date','cl_time',]
    search_fields = ['job_cat']


class CustomExportMixin(ExportMixin):
    formats = DEFAULT_FORMATS


class CareerResource(resources.ModelResource):
    class Meta:
        model = AppliedJobs


class AppliedAdmin(CustomExportMixin,admin.ModelAdmin):
    resource_class = CareerResource
    model = AppliedJobs
    list_display = ['designation','name','tele','upload_file_link']
    list_filter = ['job_cat','date']
    search_fields = ['designation']

class JobCategoryAdmin(TranslationAdmin):
    model = JobCategory


class CareerInfoAdmin(TranslationAdmin):
    model = CareerInfo
    list_display = ('site', 'title')

class CVModelAdmin(admin.ModelAdmin):
    list_display = ('created',)
    date_hierarchy = 'created'


class VacancyAdmin(TranslationAdmin):
    list_display = ('position', 'id', 'last_date', 'is_published', 'sort')
    list_editable = ('is_published', 'sort')
    list_filter = ['is_published', 'last_date']
    search_fields = ('position',)
    date_hierarchy = 'created'


admin.site.register(Career,CareerAdmin)
admin.site.register(JobCategory,JobCategoryAdmin)
admin.site.register(AppliedJobs,AppliedAdmin)
admin.site.register(CareerInfo,CareerInfoAdmin)
admin.site.register(SVModel, CVModelAdmin)
admin.site.register(Vacancy, VacancyAdmin)
