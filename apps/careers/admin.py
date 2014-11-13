from __future__ import unicode_literals
from django.contrib import admin

from import_export.admin import ExportMixin
from import_export.formats import base_formats
from modeltranslation.admin import TranslationAdmin

from apps.careers.models import CareerInfo, SVModel, Vacancy, Nationality, VacancyApply

DEFAULT_FORMATS = (
    base_formats.CSV,
    base_formats.XLS,
    base_formats.TSV,
    base_formats.ODS,
    base_formats.JSON,
    base_formats.YAML,
)


class CustomExportMixin(ExportMixin):
    formats = DEFAULT_FORMATS


class CareerInfoAdmin(TranslationAdmin):
    model = CareerInfo
    list_display = ('site', 'title')


class CVModelAdmin(admin.ModelAdmin):
    list_display = ('created', 'cv_file_link',)
    date_hierarchy = 'created'


class VacancyAdmin(TranslationAdmin):
    list_display = ('position', 'id', 'last_date', 'is_published', 'sort')
    list_editable = ('is_published', 'sort')
    list_filter = ['is_published', 'last_date']
    search_fields = ('position',)
    date_hierarchy = 'created'


class NationalityAdmin(TranslationAdmin):
    list_display = ('nationality',)


class VacancyApplyAdmin(CustomExportMixin, admin.ModelAdmin):
    list_display = ('site', 'vacancy', 'created', 'name', 'email', 'cv_file_link')
    list_filter = ['vacancy', 'site', 'created']
    search_fields = ('position',)
    date_hierarchy = 'created'


admin.site.register(SVModel, CVModelAdmin)
admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Nationality, NationalityAdmin)
admin.site.register(VacancyApply, VacancyApplyAdmin)
