from __future__ import unicode_literals
from django.views.generic import RedirectView, ListView
from django.core.urlresolvers import reverse
from django.http import Http404
from apps.project.models import Category, Project


class RedirectCategory(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        category = Category.objects.all()[0].slug
        return reverse('proj_list', kwargs={'category': category})


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
