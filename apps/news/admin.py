from __future__ import unicode_literals

from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from apps.news.models import NewsModel, NewsInfo


class NewsAdmin(TranslationAdmin):
    model = NewsModel
    list_display = ('title', 'description', 'image')
    list_editable = ('image',)
    exclude = ('year', 'date',)


class NewsInfoAdmin(TranslationAdmin):
    model = NewsInfo
    list_display = ('title', 'header_image',)

admin.site.register(NewsModel, NewsAdmin)
admin.site.register(NewsInfo, NewsInfoAdmin)
