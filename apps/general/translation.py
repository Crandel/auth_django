from modeltranslation.translator import translator, TranslationOptions
from models import FooterSettings, BannerImages, TopMenuUrl


class FooterSettingsTranslationOptions(TranslationOptions):
    fields = ('copyright',)

translator.register(FooterSettings, FooterSettingsTranslationOptions)


class BannerImagesTranslationOptions(TranslationOptions):
    fields = ('title',)

translator.register(BannerImages, BannerImagesTranslationOptions)


class TopMenuUrlTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(TopMenuUrl, TranslationOptions)
