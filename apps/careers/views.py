import json
import datetime

from django.utils import timezone
from django.views.generic import TemplateView, ListView, View, CreateView
from django.contrib.sites.models import Site
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, Http404
from django.utils.translation import ugettext_lazy as _
from django.core.mail import EmailMessage
from django.conf import settings
from django.template import Context, RequestContext, loader
from django.template.loader import render_to_string


from apps.general.models import AdminEmails
from apps.utility_files.shortcuts import send_generic_mail
from apps.careers.forms import CareerForm, CVForm, VacancyApplyForm
from apps.careers.models import Career, JobCategory, CareerInfo, Vacancy, SVModel, VacancyApply, Nationality


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
        print kwargs.get('data', None)
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


class CareerView(TemplateView):
    template_name = "careers/career.html"
    """
    Customized template view to manage content of Career page.
    """
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(CareerView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        category_list =[]
        careers = None
        categ = self.request.GET.get('categories')
        context = super(CareerView, self).get_context_data(**kwargs)
        job_cats = JobCategory.objects.all()
        current_site = Site.objects.get_current()
        if categ == 'all':
            careers = Career.objects.filter(site=current_site).filter(is_published=True).filter(cl_time__gte=datetime.datetime.now())
            context['careers'] =  careers
        if categ:
            try:
                job_cat = JobCategory.objects.get(catog=categ)
                careers = Career.objects.filter(site=current_site).filter(is_published=True).filter(job_cat=job_cat).filter(cl_time__gte=datetime.datetime.now())
            except:
                pass
            context['careers'] =  careers
        else:
            try:
                careers = Career.objects.filter(site=current_site).filter(is_published=True).filter(cl_time__gte=datetime.datetime.now())
                context['careers'] =  careers
            except Career.DoesNotExist:
                careers=None
        try:
            career_list = Career.objects.filter(site=current_site).filter(is_published=True).filter(cl_time__gte=datetime.datetime.now())
        except:
            pass
        if career_list:
            [category_list.append(career_cat.job_cat.catog) for career_cat in career_list if career_cat.job_cat.catog not in category_list]
        context['career_count'] = int(careers.count()/2)
        carrer_info = CareerInfo.objects.get(site=current_site)
        context['job_cats'] = job_cats
        context['carrer_info'] = carrer_info
        context['form'] = CareerForm()
        context['category_list'] = category_list
        return context


    def post(self,args,**kwargs):
        context = {}
        current_site = Site.objects.get_current()
        if self.request.method=='POST':
            career_form = CareerForm(self.request.POST,self.request.FILES,)
            job_cat_id =self.request.POST.get('job_cat')
            if career_form.is_valid():
                design = career_form.cleaned_data['designation']
                name = career_form.cleaned_data['name']
                email = career_form.cleaned_data['email']
                tele = career_form.cleaned_data['tele']
                upload_file = self.request.FILES['upload_file']
                form_obj = career_form.save(commit=False)
                form_obj.site = current_site
                form_obj.date = timezone.now()
                if job_cat_id:
                    jobcat = JobCategory.objects.get(id = job_cat_id )
                    print jobcat,'vvvvvvvvvvvvvv'
                    form_obj.job_cat = jobcat
                context['designation'] = design
                form_obj.save()
                admin_emails = AdminEmails.objects.get(site=current_site)
                send_generic_mail(template ="careers/career_to_user.html",context_dict = {'site':current_site,'designation':design,},subject='Career Notification.',to=email)
                subject = _('Job Application.')
#                send_generic_mail(template ="careers/career_email_to_admin.html",context_dict=admin_context,subject=subject,to=admin_emails.career_email)
                admin_context = {'name':name,'email':email,'designation':design,'telephone':tele,'site':current_site,}
                admin_template=loader.get_template('careers/career_email_to_admin.html')
                c = Context(admin_context)
                content=admin_template.render(c)
                email = EmailMessage(subject, content, settings.DEFAULT_FROM_EMAIL,[admin_emails.career_email,])
                email.content_subtype='html'
                email.attach(upload_file.name, upload_file.read(), upload_file.content_type)
                email.send()
                succes_message = _('You have successfully applied for the post of  %(desin)s.') % {'desin':design}
                context['success'] = unicode(succes_message)
                context['status'] = True

            else:
                context['errors'] = career_form.errors
                context['status'] = False
        return HttpResponse(json.dumps({'context':context}),mimetype='application/json')
