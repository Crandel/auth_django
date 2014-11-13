import json
import datetime

from django.views.generic import ListView, View, CreateView
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404
from django.template import RequestContext
from django.template.loader import render_to_string

from apps.careers.forms import CVForm, VacancyApplyForm
from apps.careers.models import CareerInfo, Vacancy, SVModel, VacancyApply, Nationality


class VacancyList(ListView):
    template_name = 'careers/careers_list.html'
    model = Vacancy
    paginate_by = 3
    site = Site.objects.get_current()
    context_object_name = "vacancies"

    def get_queryset(self):
        return self.model.objects.filter(is_published=True, site=self.site, last_date__gte=datetime.datetime.now())

    def get_context_data(self, **kwargs):
        context = super(VacancyList, self).get_context_data(**kwargs)
        context['info'] = CareerInfo.objects.get(site=self.site)
        return context


class LoadMoreVacancy(View):

    def get(self, request, *args, **kwargs):
        if not request.is_ajax():
            raise Http404
        page = int(request.GET.get('page', None))
        if not page:
            raise Http404

        self.site = Site.objects.get_current()

        vacancies = Vacancy.objects.filter(is_published=True, site=self.site, last_date__gte=datetime.datetime.now())
        if len(vacancies) > page * 3 + 3:
            load_more = True
        else:
            load_more = False

        vacancies = vacancies[page * 3: page * 3 + 3]

        html = render_to_string('careers/more_vacancy.html', {'vacancies': vacancies, 'page': page * 3},
                                context_instance=RequestContext(request))

        more = render_to_string('careers/more_button.html', {'load_more': load_more, 'page': page + 1},
                                context_instance=RequestContext(request))

        return HttpResponse(
            json.dumps({'items': html, 'more': more}),
            content_type='application/json')


class SendCV(CreateView):
    model = SVModel
    form_class = CVForm

    def form_valid(self, form):
        if not self.request.is_ajax():
            raise Http404
        cv = form.save(commit=False)
        cv.save()
        return HttpResponse(
            json.dumps({'success': True}),
            content_type='application/json')

    def form_invalid(self, form):
        if not self.request.is_ajax():
            raise Http404
        return HttpResponse(
            json.dumps({'success': False}),
            content_type='application/json')


class VacancyApplyView(CreateView):
    form_class = VacancyApplyForm
    model = VacancyApply
    template_name = "careers/vacancy_apply.html"
    site = Site.objects.get_current()

    def get_form_kwargs(self):
        kwargs = super(VacancyApplyView, self).get_form_kwargs()
        pk = self.kwargs.get('pk', None)
        if not pk:
            raise Http404
        position = Vacancy.objects.get(pk=pk)
        posit_dict = {
            'vacancy': position.id,
            'position': position.position,
            'site': self.site.pk
        }
        kwargs['initial'].update(posit_dict)
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(VacancyApplyView, self).get_context_data(**kwargs)
        context['info'] = CareerInfo.objects.get(site=self.site)
        return context

    def get_success_url(self):
        pk = self.kwargs.get('pk', None)
        return reverse('vacancy_apply', kwargs={'pk': pk})

    def form_valid(self, form):
        form.save()
        form.send_mail()
        info = CareerInfo.objects.get(site=self.site)
        return self.render_to_response({'success': True, 'info': info})


class SelectNationality(View):

    def get(self, request, *args, **kwargs):
        str_req = request.GET.get('str', None)
        if not request.is_ajax():
            raise Http404
        nat = list()
        for n in Nationality.objects.filter(nationality__icontains=str_req):
            nat.append({
                'id': n.pk,
                'name': n.nationality})
        return HttpResponse(
            json.dumps(nat),
            content_type='application/json')
