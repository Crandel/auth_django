from __future__ import unicode_literals
import re
import datetime
from django.utils import timezone
from django import forms
from captcha.fields import ReCaptchaField
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site
from django.core.mail import EmailMessage
from django.template import Context, loader
from django.core.urlresolvers import reverse_lazy
from apps.utility_files.shortcuts import send_generic_mail
from apps.general.models import AdminEmails
from apps.careers.models import AppliedJobs,Career, SVModel, VacancyApply


class CareerForm(forms.ModelForm):
    captcha = ReCaptchaField(attrs={'theme' : 'white'})
    """
    Form to shows the year on news event page .

    """

    class Meta:
        model = AppliedJobs
        exclude = ['site','date','job_cat']

    def clean_tele(self):
        tele = self.cleaned_data['tele']
        if not tele.isdigit():
            raise forms.ValidationError(_("Please enter digits only!"))
        if len(tele) < 8 or len(tele) > 15:
            raise forms.ValidationError(_("Please enter digits between 8 to 15!"))
        return tele

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name.strip())<=1:
            raise forms.ValidationError(_("Please enter your name."))
        return name

    def clean_upload_file(self):
        upload_file = self.cleaned_data['upload_file']
        extention = str(upload_file).split('.')[-1]
        if extention not in settings.ACCEPTED_CV_FORMATS:
            raise forms.ValidationError(_("Invalid file format.."))
        return upload_file


class CareerAdminForm(forms.ModelForm):

    class Meta:
        model = Career

    def clean_cl_time(self):
        closing_date = self.cleaned_data['cl_time']
        created_date = self.cleaned_data['date']
        if closing_date <= created_date:
            raise forms.ValidationError(_("Please enter valid closing date."))
#        elif closing_date <= timezone.now():
#            raise forms.ValidationError(_("Please enter valid closing date."))
        return closing_date


class CVForm(forms.ModelForm):

    class Meta:
        model = SVModel

    def save(self, commit=True):
        if commit:
            f = self.cleaned_data['cv']
            current_site = Site.objects.get_current()
            admin_emails = AdminEmails.objects.get(site=current_site)
            subject = _('Send new CV')
            admin_context = {}
            admin_template = loader.get_template('careers/career_email_to_admin.html')
            c = Context(admin_context)
            content = admin_template.render(c)
            email = EmailMessage(subject, content, settings.DEFAULT_FROM_EMAIL, [admin_emails.career_email])
            email.content_subtype = 'html'
            if f:
                email.attach(f.name, f.read(), f.content_type)
            email.send()
        return super(CVForm, self).save(self)


class VacancyApplyForm(forms.ModelForm):
    captcha = ReCaptchaField()
    nationality_name = forms.CharField()

    class Meta:
        model = VacancyApply
        widgets = {
            'vacancy': forms.HiddenInput(),
            'site': forms.HiddenInput(),
            'position': forms.TextInput(attrs={'readonly': 'readonly'}),
            'nationality': forms.HiddenInput(attrs={'class': 'required', 'data-settings': '{"cutOff":10}'}),
            'nationality_name': forms.TextInput(attrs={'data-url': reverse_lazy('select_nat')}),
            'name': forms.TextInput(attrs={'class': 'required'}),
            'address': forms.Textarea(attrs={'class': 'required'}),
            'phone': forms.TextInput(attrs={'class': 'required'}),
            'email': forms.TextInput(attrs={'class': 'required'}),
        }

    def clean_phone(self):
        '''
        Checks phone number field against a regular expression.

        :return: string
        :type: forms.CharField
        :except: ValidationError
        '''
        phone_digits = re.compile(r'^[0-9\-\+]{9,15}$')
        value = self.cleaned_data.get("phone")
        match = phone_digits.match(value)
        if match:
            return value
        raise forms.ValidationError(
            _('Phone numbers must be in +{XXX} XXX XXX-XX-XX,\
            XXX-XXX-XX-XX, or (XXX) XXX-XX-XX format or other phone format.'),
        )

    def send_mail(self):
        current_site = Site.objects.get_current()
        admin_emails = AdminEmails.objects.get(site=current_site)
        context = {}
        company_name = self.cleaned_data['position']
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        phone = self.cleaned_data['phone']
        address = self.cleaned_data['address']
        subject = 'Thanks for contacting us!'
        subject_admin = 'Contact details via %s' % (current_site.name)
        context = {
            'name': name,
            'company_name': company_name,
            'email': email,
            'address': address,
            'phone': phone,
            'date': datetime.datetime.now(),
            'site': current_site}
        send_generic_mail(template="careers/career_to_user.html", context_dict=context, subject=subject, to=email)
        send_generic_mail(
            template="careers/career_email_to_admin.html",
            context_dict=context,
            subject=subject_admin,
            to=admin_emails.con_email)
