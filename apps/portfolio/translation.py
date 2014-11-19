from modeltranslation.translator import translator, TranslationOptions
from apps.portfolio.models import PortfolioInfo, Category, Project, Image


class PortfolioInfoTranslationOptions(TranslationOptions):
    fields = ('title',)


class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'client', 'location', 'scope', 'description')


class ImageTranslationOptions(TranslationOptions):
    fields = ('title',)


translator.register(PortfolioInfo, PortfolioInfoTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
translator.register(Project, ProjectTranslationOptions)
translator.register(Image, ImageTranslationOptions)