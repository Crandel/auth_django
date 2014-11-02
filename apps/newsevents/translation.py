from modeltranslation.translator import translator, TranslationOptions
from models import Events, News

class NewsTranslationOptions(TranslationOptions):
    fields = ('news_title','news_desc',)

class EventsTranslationOptions(TranslationOptions):
    fields = ('event_title','event_desc')

translator.register(News, NewsTranslationOptions)
translator.register(Events, EventsTranslationOptions)