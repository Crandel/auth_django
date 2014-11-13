from modeltranslation.translator import translator, TranslationOptions
from models import CareerInfo, JobCategory, Career, Vacancy, Nationality


class CareerInfoTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


class JobCategoryTranslationOptions(TranslationOptions):
    fields = ('catog',)


class CareerTranslationOptions(TranslationOptions):
    fields = ('designation', 'short_desc',)


class VacancyTranslationOption(TranslationOptions):
    fields = ('position', 'requirement')


class NationalityTranslationOptions(TranslationOptions):
    fields = ('nationality',)

translator.register(CareerInfo, CareerInfoTranslationOptions)
translator.register(JobCategory, JobCategoryTranslationOptions)
translator.register(Career, CareerTranslationOptions)
translator.register(Vacancy, VacancyTranslationOption)
translator.register(Nationality, NationalityTranslationOptions)
