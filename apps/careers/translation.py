from modeltranslation.translator import translator, TranslationOptions
from models import CareerInfo,JobCategory,Career

class CareerInfoTranslationOptions(TranslationOptions):
    fields = ('title','description',)

class JobCategoryTranslationOptions(TranslationOptions):
    fields = ('catog',)

class CareerTranslationOptions(TranslationOptions):
    fields = ('designation','short_desc',)

translator.register(CareerInfo, CareerInfoTranslationOptions)
translator.register(JobCategory, JobCategoryTranslationOptions)
translator.register(Career, CareerTranslationOptions)