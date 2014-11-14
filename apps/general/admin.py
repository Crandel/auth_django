from django.contrib import admin
from django.template.loader import render_to_string
from modeltranslation.admin import TranslationAdmin
from apps.general.models import FooterSettings, CommonSettings, AdminEmails, BannerImages, TopMenuUrl

class FooterSettingsAdmin(TranslationAdmin):
    model = FooterSettings


class BannerImagesAdmin(TranslationAdmin):
    """
    Admin class for banner images
    """
    list_display = ('banner_image', 'sort_order', 'published', 'admin_thumbnail')
    list_editable = ('sort_order', 'published',)

    def banner_image(self, obj):
        return  render_to_string('thumb.html',{
                    'image': obj.image
                })

    banner_image.allow_tags = True


class TopMenuUrlAdmin(TranslationAdmin):
    list_display = ('name', 'site', 'sort')
    list_editable = ('sort',)


admin.site.register(FooterSettings,FooterSettingsAdmin)
admin.site.register(CommonSettings)
admin.site.register(AdminEmails)
admin.site.register(BannerImages, BannerImagesAdmin)
admin.site.register(TopMenuUrl, TopMenuUrlAdmin)
