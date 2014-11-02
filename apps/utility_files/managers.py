from django.db import models


class BrowsableManager(models.Manager):
    def get_query_set(self):
        return super(BrowsableManager, self).get_query_set().filter(
            published=True)
