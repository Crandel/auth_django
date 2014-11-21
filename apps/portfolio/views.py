from django.views.generic import ListView, View
from apps.portfolio.models import PortfolioInfo, Category, Project
from django.contrib.sites.models import Site
from django.http import HttpResponse, Http404


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
