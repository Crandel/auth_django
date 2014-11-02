from haystack import indexes
from models import Career


class CareerIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    designation = indexes.CharField(model_attr='designation')
    short_desc = indexes.CharField(model_attr='short_desc')

    def get_model(self):
        return Career

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()