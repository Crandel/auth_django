from __future__ import unicode_literals
import json

from django.template.context import RequestContext
from django.template.loader import render_to_string
from django.views.generic import TemplateView, View
from django.http import HttpResponse, Http404

from apps.news.models import NewsModel, NewsInfo


class NewsList(TemplateView):
    template_name = 'news/news_list.html'

    def get_context_data(self, **kwargs):
        context = super(NewsList, self).get_context_data(**kwargs)

        years = NewsModel.objects.values_list('year', flat=True).distinct()
        context['years'] = years
        year = int(self.kwargs.get('year', years[0]))

        if year not in years:
            year = years[0]
        # take all news from selected year
        context['selected_year'] = year
        all_filtered_news = NewsModel.objects.filter(year=year).order_by('-created_at')
        # take only months
        months = list({m.created_at.month for m in all_filtered_news})
        months.sort()

        if len(months) > 6:
            context['more'] = months[-6]

        # list with news for last 6 months
        news = [new for new in all_filtered_news if new.created_at.month in months[-6:]]
        context['news'] = news
        context['news_info'] = NewsInfo.objects.all()
        return context


class LoadMore(View):

    def get(self, request, *args, **kwargs):
        if not request.is_ajax():
            return Http404

        month = int(request.GET.get('month', None))
        year = int(request.GET.get('year', None))
        if not month and not year:
            return Http404


        all_filtered_news = NewsModel.objects.filter(year=year).order_by('-created_at')
        news = [new for new in all_filtered_news if new.created_at.month < month]
        html = render_to_string('news/more_news.html', {'news': news},
                                context_instance=RequestContext(request))

        return HttpResponse(
            json.dumps({'news': html}),
            content_type='application/json')
