from haystack import indexes
from apps.project.models import Project


class ProjectIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    project = indexes.CharField(model_attr='project')
    description = indexes.CharField(model_attr='description')

    def get_model(self):
        return Project

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(publish=True)
