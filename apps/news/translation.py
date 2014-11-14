from __future__ import unicode_literals
from modeltranslation.translator import translator, TranslationOptions
from apps.news.models import News, NewsInfo


class NewsInfoTranslationOptions(TranslationOptions):
    fields = ('title',)


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


translator.register(NewsInfo, NewsInfoTranslationOptions)
translator.register(News, NewsTranslationOptions)



