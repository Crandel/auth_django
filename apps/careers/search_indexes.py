import datetime
from haystack import indexes
from apps.careers.models import Vacancy


class VacancyIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    position = indexes.CharField(model_attr='position')
    requirement = indexes.CharField(model_attr='requirement')

    def get_model(self):
        return Vacancy

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(is_published=True, last_date__gte=datetime.datetime.now())
