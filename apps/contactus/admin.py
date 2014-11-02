from django.contrib import admin
from apps.contactus.models import ContactUs,GoogleContact
from import_export import resources

from import_export.admin import ExportMixin
from import_export.formats import base_formats

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

class ContactResource(resources.ModelResource):
    class Meta:
        model = ContactUs

class ContactAdmin(CustomExportMixin,admin.ModelAdmin):
    resource_class = ContactResource
    model=ContactUs
    list_display = ['name','email',]
    search_fields = ['name','email']
    list_filter = ['date']
admin.site.register(ContactUs,ContactAdmin)
admin.site.register(GoogleContact)
