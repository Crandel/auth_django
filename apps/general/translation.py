from modeltranslation.translator import translator, TranslationOptions
from models import FooterSettings, BannerImages


class FooterSettingsTranslationOptions(TranslationOptions):
    fields = ('copyright',)

translator.register(FooterSettings, FooterSettingsTranslationOptions)


class BannerImagesTranslationOptions(TranslationOptions):
    fields = ('title',)

translator.register(BannerImages, BannerImagesTranslationOptions)
