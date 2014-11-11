from __future__ import unicode_literals
from modeltranslation.translator import translator, TranslationOptions
from apps.project.models import Category, Project, Image


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Category, CategoryTranslationOptions)


class ProjectTranslationOptions(TranslationOptions):
    fields = ('project', 'client', 'location', 'scope', 'description')

translator.register(Project, ProjectTranslationOptions)


class ImagesTranslationOptions(TranslationOptions):
    fields = ('title',)

translator.register(Image, ImagesTranslationOptions)
