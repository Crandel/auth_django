from modeltranslation.translator import translator, TranslationOptions
from apps.portfolio.models import PortfolioInfo, Category, Project


class PortfolioInfoTranslationOptions(TranslationOptions):
    fields = ('title',)


class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'client', 'location', 'scope', 'description')


translator.register(PortfolioInfo, PortfolioInfoTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
translator.register(Project, ProjectTranslationOptions)