import datetime

from captcha.fields import ReCaptchaField
from django import forms
from models import ContactUs
from django.contrib.sites.models import Site
from apps.utility_files.shortcuts import send_generic_mail
from django.utils.translation import ugettext_lazy as _
from apps.general.models import AdminEmails

class ContactUsForm(forms.ModelForm):
    """
    Form to user fill the contact details in contact us page.
    """
    captcha = ReCaptchaField(attrs={'lang':'en'})
    class Meta:
        model = ContactUs
        exclude =('site','date')
    def __init__(self, *args, **kwargs):
        super(ContactUsForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'input required'
        self.fields['company_name'].widget.attrs['class'] = 'input required'
        self.fields['email'].widget.attrs['class'] = 'input required'
        self.fields['telephone'].widget.attrs['class'] = 'input required'
        self.fields['subject'].widget.attrs['class'] = 'input required'
        self.fields['details'].widget.attrs['class'] = 'bdr-none requried'

    def clean_telephone(self):
        tele = self.cleaned_data['telephone']
        if not tele.isdigit():
            raise forms.ValidationError(_("Please enter digits only!"))
        if len(tele) < 8 or len(tele) > 15:
            raise forms.ValidationError(_("Please enter digits between 8 to 15!"))
        return tele

    def save(self):
        instance = super(ContactUsForm, self).save(commit=False)
        current_site = Site.objects.get_current()
        instance.site = current_site
        instance.save()

    def send_mail(self):
        current_site = Site.objects.get_current()
        admin_emails = AdminEmails.objects.get(site=current_site)
        context = {}
        name = self.cleaned_data['name']
        company_name = self.cleaned_data['company_name']
        email = self.cleaned_data['email']
        tele = self.cleaned_data['telephone']
        subject = self.cleaned_data['subject']
        details = self.cleaned_data['details']
        subject = 'Thanks for contacting us!'
        subject_admin = 'Contact details via %s' % (current_site.name)
        context = {
            'name': name,
            'company_name': company_name,
            'email': email,
            'subject': subject,
            'telephone': tele,
            'details': details,
            'date': datetime.datetime.now(),
            'site': current_site}
        send_generic_mail(template="contactus/contact_email_to_user.html", context_dict=context, subject=subject, to=email)
        send_generic_mail(
            template="contactus/contact_email_to_admin.html",
            context_dict=context,
            subject=subject_admin,
            to=admin_emails.con_email)


