from __future__ import unicode_literals
import json
from django.views.generic import RedirectView, ListView, DetailView, View
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponse
from django.template.loader import render_to_string
from django.template import RequestContext
from django.contrib.sites.models import Site
from apps.project.models import Category, Project, PortfolioInfo


class PortfolioPage(ListView):
    template_name = 'project/portfolio.html'
    model = Category
    context_object_name = 'categories'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super(PortfolioPage, self).get_context_data(**kwargs)
        categories = self.get_queryset()
        cat_list = [list(categories[i * 10: i * 10 + 10]) for i in range((len(categories) / 10) + 1)]
        if len(cat_list[len(cat_list) - 1]) == 0:
            cat_list.pop(len(cat_list) - 1)
        category_list = []
        for cat in cat_list:
            category_list.append([cat[0:5], cat[5:]])
        context['category_menu'] = category_list
        current_site = Site.objects.get_current
        context['info'] = PortfolioInfo.objects.get(site=current_site)
        return context


class ProjectListDetail(ListView):
    template = 'project/project_list.html'
    model = Project
    paginate_by = 8
    context_object_name = 'projects'

    def get_current_category(self):
        slug = self.kwargs.get('category', None)
        try:
            self.category = Category.objects.get(slug=slug)
        except Category.DoesNotExist:
            raise Http404
        return True

    def get_context_data(self, **kwargs):
        context = super(ProjectListDetail, self).get_context_data(**kwargs)
        categories = Category.objects.all()
        cat_list = [list(categories[i * 10: i * 10 + 10]) for i in range((len(categories) / 10) + 1)]
        if len(cat_list[len(cat_list) - 1]) == 0:
            cat_list.pop(len(cat_list) - 1)
        category_list = []
        for cat in cat_list:
            category_list.append([cat[0:5], cat[5:]])
        context['category_menu'] = category_list
        context['categories'] = categories
        try:
            self.category
        except AttributeError:
            self.get_current_category()
        context['category'] = self.category
        return context

    def get_queryset(self):
        try:
            self.category
        except AttributeError:
            self.get_current_category()
        return Project.objects.filter(publish=True, category=self.category).prefetch_related('images')


class ProjectDetail(DetailView):
    model = Project
    template_name = 'project/project_detail.html'

    def get_current_category(self):
        slug = self.kwargs.get('category', None)
        try:
            self.category = Category.objects.get(slug=slug)
        except Category.DoesNotExist:
            raise Http404
        return True

    def get_context_data(self, **kwargs):
        context = super(ProjectDetail, self).get_context_data(**kwargs)
        categories = Category.objects.all()
        cat_list = [list(categories[i * 10: i * 10 + 10]) for i in range((len(categories) / 10) + 1)]
        if len(cat_list[len(cat_list) - 1]) == 0:
            cat_list.pop(len(cat_list) - 1)
        category_list = []
        for cat in cat_list:
            category_list.append([cat[0:5], cat[5:]])
        context['category_menu'] = category_list
        try:
            self.category
        except AttributeError:
            self.get_current_category()
        context['category'] = self.category
        context['projects'] = Project.objects.filter(publish=True, category=self.category)
        return context


class LoadMoreProject(View):

    def get(self, request, *args, **kwargs):
        if not request.is_ajax():
            raise Http404
        page = int(request.GET.get('page', None))
        category = kwargs.get('category', None)
        if not page or not category:
            raise Http404

        projects = Project.objects.filter(publish=True, category__slug=category)
        if len(projects) > page * 8 + 8:
            load_more = True
        else:
            load_more = False

        projects = projects[page * 8: page * 8 + 8]

        html = render_to_string('project/more_projects.html', {'projects': projects},
                                context_instance=RequestContext(request))

        more = render_to_string('project/more_button.html', {'load_more': load_more, 'page': page + 1, 'categoty': category},
                                context_instance=RequestContext(request))

        return HttpResponse(
            json.dumps({'items': html, 'more': more}),
            content_type='application/json')


class LoadMoreCategory(View):

    def get(self, request, *args, **kwargs):
        if not request.is_ajax():
            raise Http404
        page = int(request.GET.get('page', None))
        if not page:
            raise Http404

        categories = Category.objects.all()
        if len(categories) > page * 12 + 12:
            load_more = True
        else:
            load_more = False

        categories = categories[page * 12: page * 12 + 12]

        html = render_to_string('project/more_category.html', {'categories': categories},
                                context_instance=RequestContext(request))

        more = render_to_string('project/more_button.html', {'load_more': load_more, 'page': page + 1},
                                context_instance=RequestContext(request))

        return HttpResponse(
            json.dumps({'items': html, 'more': more}),
            content_type='application/json')
