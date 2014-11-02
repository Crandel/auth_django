
from haystack import indexes
from models import Events,News


class EventsIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    event_title = indexes.CharField(model_attr='event_title')
    event_desc = indexes.CharField(model_attr='event_desc')

    def get_model(self):
        return Events

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()


class NewsIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    news_title = indexes.CharField(model_attr='news_title')
    news_desc = indexes.CharField(model_attr='news_desc')

    def get_model(self):
        return News

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()