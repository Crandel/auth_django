import json

from django.views.generic.base import TemplateView
from apps.newsevents.models import *
from django.contrib.sites.models import Site
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.http import HttpResponse
from forms import NewsForm


class EventsView(TemplateView):
    template_name = "newsevents/events.html"
    """
    Customized template view to manage content of News event page.
    """
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(EventsView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        new_list = []
        year_id = self.request.GET.get('year')
        sitco_news_id = self.request.GET.get('sitco_news_id')
        intial_news = None       
        context = super(EventsView, self).get_context_data(**kwargs)
        current_site = Site.objects.get_current()
        events = Events.objects.filter(site = current_site).filter(is_published=True)
        if year_id:
            try:
                news_yearobj = NewsYear.objects.get(news_year = year_id)
                news = News.objects.filter(site = current_site).filter(is_published=True).filter(news_year=news_yearobj)                                
                context['news'] = news
            except News.DoesNotExist:
                news = None
            if news:
                intial_news = news[0]
                context['intial_news'] = intial_news

        elif sitco_news_id:
            try:
                intial_news = News.objects.get(id=sitco_news_id)
                context['intial_news']=intial_news
                newsyearobj = NewsYear.objects.get(news_year=intial_news.news_year)
                news = News.objects.filter(site = current_site).filter(is_published=True).filter(news_year=newsyearobj)
                context['news']=news
            except:
                pass
        else:
            try:
                news = News.objects.filter(site = current_site).filter(is_published=True)
                intial_news = news[0]
                context['intial_news']=intial_news
                context['news']=news
            except:
               news = None
        try:
            all_news = News.objects.all()
        except News.DoesNotExist:
            pass
        if all_news:
            [new_list.append(news.news_year.news_year)
            for news in all_news if news.news_year.news_year not in new_list]
            sorted_year = sorted(new_list, reverse=True)
        context['events']=events                
        context['form'] = NewsForm()
        context['new_list'] = sorted_year
#        context['newdrop'] = newdrop
        return context

    def post(self,args,**kwargs):
        news_id = self.request.POST['news_id']        
        try:
            news_obj = News.objects.get(id=news_id)
        except News.DoesNotExist:
            pass
        context = self.get_context_data()
        context['html'] = render_to_string('newsevents/ajax_content.html', {
                                    'news_obj': news_obj,
                            })
        return HttpResponse(json.dumps({'context':context['html'],}),mimetype='application/json')