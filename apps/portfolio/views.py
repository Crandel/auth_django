import json
from django.shortcuts import get_object_or_404
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
        # generator for submenu
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


class LoadMoreProj(View):

    def get(self, request, *args, **kwargs):
        if not request.is_ajax():
            raise Http404

        page = int(request.GET.get('page', None))
        if not page:
            raise Http404

        self.site = Site.objects.get_current()

        projects = Project.objects.all()
        if len(projects) > (page + 1) * 8:
            load_more = True
        else:
            load_more = False

        projects = projects[page * 8: (page + 1) * 8]

        html = render_to_string('project/more_projects.html', {'projects': projects},
                                context_instance=RequestContext(request))

        more = render_to_string('project/more_button.html', {'load_more': load_more, 'page': page + 1},
                                context_instance=RequestContext(request))

        return HttpResponse(
            json.dumps({'items': html, 'more': more}),
            content_type='application/json')


class ProjectList(ListView):
    """docstring for ProjectList"""
    template_name = 'project/project_list.html'
    model = Project
    paginate_by = 8
    context_object_name = 'projects'
    category = None

    def get_context_data(self, **kwargs):
        context = super(ProjectList, self).get_context_data(**kwargs)
        context['category'] = self.get_category()
        queryset = Category.objects.all()
        # generator for submenu
        first_list = [
            queryset[c * 6: (c + 1) * 6]
            for c in range((len(queryset) + 5) / 6)
        ]
        context['submenu_list'] = first_list
        return context


    def get_queryset(self):
        return super(ProjectList, self).get_queryset().filter(category=self.get_category())

    def get_category(self):
        if self.category:
            return self.category
        category_id = self.kwargs.get('category', None)
        if not category_id:
            raise Http404
        self.category = get_object_or_404(Category, slug=category_id)
        return self.category