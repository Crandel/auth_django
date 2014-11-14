from __future__ import unicode_literals
import json
import datetime
import calendar
from django.views.generic import TemplateView, View
from django.contrib.sites.models import Site
from django.http import Http404, HttpResponse
from django.template import RequestContext
from django.template.loader import render_to_string

from apps.news.models import NewsInfo, News


class NewsView(TemplateView):

    template_name = 'news/news_list.html'
    site = Site.objects.get_current()
    news_more = False

    def group_news(self, qs, year):
        news = qs.filter(date_time__year=str(year))
        year = int(year)
        monthes = sorted(list(set([m.date_time.month for m in news])))
        if len(monthes) > 6:
            self.news_more = True
        news_list = []
        for m in monthes[:6]:
            last_day_of_month = calendar.monthrange(year, 11)[1]
            first_day = datetime.date(year, m, 1)
            last_day = datetime.date(year, m, last_day_of_month)
            month_news = [n for n in news.filter(date_time__gte=first_day, date_time__lte=last_day)]
            if len(month_news):
                news_list.append({'date': first_day, 'news': month_news})
        return news_list

    def get_context_data(self, **kwargs):
        context = super(NewsView, self).get_context_data(**kwargs)
        context['info'] = NewsInfo.objects.get(site=self.site)
        news = News.objects.filter(is_published=True, site=self.site).order_by('-date_time')
        context['years'] = sorted(list(set([y.date_time.year for y in news])), reverse=True)
        year = self.kwargs.get('year', None)
        if not year:
            year = context['years'][0]
        context['year'] = int(year)
        context['news'] = self.group_news(news, year)
        context['more'] = self.news_more
        return context


class LoadMoreNews(View):
    site = Site.objects.get_current()

    def get(self, request, *args, **kwargs):
        year = request.GET.get('year', None)
        if not year or not request.is_ajax():
            raise Http404

        news = News.objects.filter(is_published=True, site=self.site, date_time__year=year).order_by('-date_time')
        year = int(year)
        monthes = sorted(list(set([m.date_time.month for m in news])))
        news_list = []
        for m in monthes[6:]:
            last_day_of_month = calendar.monthrange(year, 11)[1]
            first_day = datetime.date(year, m, 1)
            last_day = datetime.date(year, m, last_day_of_month)
            month_news = [n for n in news.filter(date_time__gte=first_day, date_time__lte=last_day)]
            if len(month_news):
                news_list.append({'date': first_day, 'news': month_news})
        html = render_to_string('news/more_news.html', {'news': news_list},
                                context_instance=RequestContext(request))

        return HttpResponse(
            json.dumps({'items': html}),
            content_type='application/json')
        return news_list

