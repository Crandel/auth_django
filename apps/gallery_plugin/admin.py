from inline_ordering.admin import OrderableStackedInline
from modeltranslation.admin import TranslationAdmin
import models


class ImageInline(OrderableStackedInline):
    model = models.GalleryImage


    