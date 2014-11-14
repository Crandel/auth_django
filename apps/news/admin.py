from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.utils.translation import ugettext_lazy as _
from modeltranslation.admin import TranslationAdmin
from apps.news.models import News, NewsInfo


class NewsInfoAdmin(TranslationAdmin):
    fields = ('site', 'title',)

admin.site.register(NewsInfo, NewsInfoAdmin)


class YearFilter(SimpleListFilter):
    title = _('Year')
    parameter_name = 'year'

    def lookups(self, request, model_admin):
        years = set([y.date_time.year for y in model_admin.model.objects.all()])
        return [(y, str(y)) for y in years]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(date_time__year=self.value())
        else:
            return queryset


class NewsAdmin(TranslationAdmin):
    list_display = ('title', 'date_time', 'is_published', 'sort_order')
    search_fields = ('title', )
    # date_hierarchy = 'date_time'
    list_filter = ('is_published', YearFilter)
    list_editable = ('is_published', 'sort_order')

admin.site.register(News, NewsAdmin)






