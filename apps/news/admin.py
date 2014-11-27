from __future__ import unicode_literals

from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from apps.news.models import NewsModel


class NewsAdmin(TranslationAdmin):
    model = NewsModel
    list_display = ('title', 'description', 'image')
    list_editable = ('image',)
    exclude = ('year', 'date',)

admin.site.register(NewsModel, NewsAdmin)