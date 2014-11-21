import json
from django.views.generic import ListView, View
from apps.portfolio.models import PortfolioInfo, Category, Project
from django.contrib.sites.models import Site
from django.http import HttpResponse, Http404
from django.template import RequestContext
from django.template.loader import render_to_string


class CategoryList(ListView):
    template_name = 'project/portfolio_info.html'
    model = Category
    paginate_by = 12
    context_object_name = 'categories'
    site = Site.objects.get_current()

    def get_context_data(self, **kwargs):
        context = super(CategoryList, self).get_context_data(**kwargs)
        context['portfolio_info'] = PortfolioInfo.objects.get(site=self.site)
        queryset = self.get_queryset()
        first_list = [
            queryset[c * 6: (c + 1) * 6]
            for c in range((len(queryset) + 5) / 6)
        ]
        context['submenu_list'] = first_list
        return context


class LoadMore(View):

    def get(self, request, *args, **kwargs):
        if not request.is_ajax():
            raise Http404

        page = int(request.GET.get('page', None))
        if not page:
            raise Http404

        self.site = Site.objects.get_current()

        categories = Category.objects.all()
        if len(categories) > page * 12 + 12:
            load_more = True
        else:
            load_more = False

        categories = categories[page * 12: (page + 1) * 12]

        html = render_to_string('project/more_cariers.html', {'categories': categories},
                                context_instance=RequestContext(request))

        more = render_to_string('project/more_button.html', {'load_more': load_more, 'page': page + 1},
                                context_instance=RequestContext(request))

        return HttpResponse(
            json.dumps({'items': html, 'more': more}),
            content_type='application/json')