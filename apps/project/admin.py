from __future__ import unicode_literals

from django.contrib import admin

from modeltranslation.admin import TranslationAdmin, TranslationStackedInline

from apps.project.models import Category, Project, Image, PortfolioInfo


class PortfolioInfoAdmin(TranslationAdmin):
    list_display = ('site', 'title')

admin.site.register(PortfolioInfo, PortfolioInfoAdmin)


class CategoryAdmin(TranslationAdmin):

    list_display = ('name', 'admin_thumbnail', 'slug', 'order')
    list_editable = ('order',)

admin.site.register(Category, CategoryAdmin)


class ImageInline(TranslationStackedInline):

    model = Image
    extra = 0


class ProjectAdmin(TranslationAdmin):
    list_display = ('project', 'category', 'publish',)
    list_filter = ('category', 'publish',)
    search_fields = ('project', 'client', 'location')
    inlines = (ImageInline,)

admin.site.register(Project, ProjectAdmin)
