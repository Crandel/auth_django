from modeltranslation.translator import translator, TranslationOptions
from models import FooterSettings

class FooterSettingsTranslationOptions(TranslationOptions):
    fields = ('copyright',)

translator.register(FooterSettings, FooterSettingsTranslationOptions)
