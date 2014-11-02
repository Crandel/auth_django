from modeltranslation.translator import translator, TranslationOptions
from models import HomeContents,HomeBanner

class HomeContentsTranslationOptions(TranslationOptions):
    fields = ('main_itle','sub_title','ceo_title','ceo_desc',)


class HomeBannerTranslationOptions(TranslationOptions):
    fields = ('banner_title',)

translator.register(HomeContents, HomeContentsTranslationOptions)
translator.register(HomeBanner, HomeBannerTranslationOptions)

