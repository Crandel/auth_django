from modeltranslation.translator import translator, TranslationOptions
from models import CareerInfo, Vacancy, Nationality


class CareerInfoTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


class VacancyTranslationOption(TranslationOptions):
    fields = ('position', 'requirement')


class NationalityTranslationOptions(TranslationOptions):
    fields = ('nationality',)

translator.register(CareerInfo, CareerInfoTranslationOptions)
translator.register(Vacancy, VacancyTranslationOption)
translator.register(Nationality, NationalityTranslationOptions)
