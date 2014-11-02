
from django.utils import timezone
from django import forms
from models import AppliedJobs,Career
from captcha.fields import ReCaptchaField
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

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



