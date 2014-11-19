from __future__ import unicode_literals
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from apps.portfolio.models import PortfolioInfo, Category, Project, Image


class ImageInline(TranslationTabularInline):
    model = Image
    extra = 0


class PortfolioInfoAdmin(TranslationAdmin):
    model = PortfolioInfo
    list_display = ('title', 'header_image')


class CategoryAdmin(TranslationAdmin):
    model = Category
    list_display = ('title', 'thumbnail_image', 'order')
    list_editable = ('order',)


class ProjectAdmin(TranslationAdmin):
    model = Project
    list_display = ('title', 'category')
    search_fields = ('title',)
    list_filter = ('category',)
    inlines = [ImageInline]


admin.site.register(PortfolioInfo, PortfolioInfoAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Project, ProjectAdmin)