from modeltranslation.translator import translator, TranslationOptions

from apps.news.models import NewsModel


class NewsModelTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


translator.register(NewsModel, NewsModelTranslationOptions)