from django.contrib import admin
from apps.newsevents.models import Events,News,NewsYear
from modeltranslation.admin import TranslationAdmin

from apps.newsevents.forms import NewsAdminForm

class EventsAdmin(TranslationAdmin):
    model= Events
    list_display = ['event_title','is_published','sort_order']
    list_filter = ['event_date_time','is_published']
    search_fields = ['event_title','event_date_time']

class NewsAdmin(TranslationAdmin):
    model = News
    form = NewsAdminForm
    list_display = ['news_title','is_published','sort_order']
    list_filter = ['news_title']
    search_fields = ['news_year','news_title']
    list_filter = ['news_year','is_published']
    
admin.site.register(Events,EventsAdmin)
admin.site.register(News,NewsAdmin)
admin.site.register(NewsYear)
