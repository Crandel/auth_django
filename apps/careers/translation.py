from modeltranslation.translator import translator, TranslationOptions
from models import CareerInfo, JobCategory, Career, Vacancy


class CareerInfoTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


class JobCategoryTranslationOptions(TranslationOptions):
    fields = ('catog',)


class CareerTranslationOptions(TranslationOptions):
    fields = ('designation', 'short_desc',)


class VacancyTranslationOption(TranslationOptions):
    fields = ('position', 'requirement')

translator.register(CareerInfo, CareerInfoTranslationOptions)
translator.register(JobCategory, JobCategoryTranslationOptions)
translator.register(Career, CareerTranslationOptions)
translator.register(Vacancy, VacancyTranslationOption)
