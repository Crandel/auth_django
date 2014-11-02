from django.contrib.flatpages.admin import FlatPageAdmin
from forms import MyFlatpageForm
from django.contrib.flatpages.models import FlatPage
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from django.utils.translation import ugettext_lazy as _

class MyFlatPageAdmin(FlatPageAdmin,TranslationAdmin):
    form = MyFlatpageForm
    filter_horizontal=['sites']

    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites','sort_order','select_link',)}),
        (_('Advanced options'), {'classes': ('collapse',), 'fields': ('enable_comments', 'registration_required', 'template_name')}),
    )
    list_display = ('url', 'title','sort_order',)
    list_filter = ('sites','select_link','registration_required')
    search_fields = ('url', 'title')

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, MyFlatPageAdmin)