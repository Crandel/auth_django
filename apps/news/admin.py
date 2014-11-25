from __future__ import unicode_literals

from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from apps.news.models import New


class NewsAdmin(TranslationAdmin):
    model = New
    list_display = ('title', 'description', 'image')