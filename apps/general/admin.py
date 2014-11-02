from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from apps.general.models import FooterSettings,CommonSettings,AdminEmails,BannerSettings

class FooterSettingsAdmin(TranslationAdmin):
    model = FooterSettings


admin.site.register(FooterSettings,FooterSettingsAdmin)
admin.site.register(CommonSettings)
admin.site.register(AdminEmails)
admin.site.register(BannerSettings)