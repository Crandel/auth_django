from django.contrib import admin
from modeltranslation.admin import TranslationAdmin,TranslationTabularInline
from apps.home.models import *


class HomeBannerInline(TranslationTabularInline):
    model = HomeBanner

class CEOImagesInline(admin.TabularInline):
    model = CEOImages
    exclude = ['image_url']

class HomeBannerAdmin(TranslationAdmin):
    inlines = [
        HomeBannerInline,
        CEOImagesInline,
    ]



admin.site.register(HomeContents, HomeBannerAdmin)

