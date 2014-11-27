from modeltranslation.translator import translator, TranslationOptions

from apps.news.models import NewsModel, NewsInfo


class NewsModelTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


class NewsInfoTranslationOptions(TranslationOptions):
    fields = ('title',)


translator.register(NewsModel, NewsModelTranslationOptions)
translator.register(NewsInfo, NewsInfoTranslationOptions)