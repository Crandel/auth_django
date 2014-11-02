from django.utils.translation import ugettext_lazy as _
from django import forms
from django.utils import timezone

from models import News,Events



class NewsForm(forms.ModelForm):
    """
    Form to shows the year on news event page .
    
    """
    
    class Meta:
        model = News
        fields = ('news_year',)

    def __init__(self, *args, **kwargs):
        super(NewsForm, self).__init__(*args, **kwargs)
        self.fields['news_year'].widget.attrs['class'] = 'dropdown'


class NewsAdminForm(forms.ModelForm):
    """
    Form to shows the year on news event page .

    """

    class Meta:
        model = News

    def clean_news_date_time(self):
        news_date = self.cleaned_data['news_date_time']
        year = self.cleaned_data['news_year']        
        if not str(news_date.year) == str(year.news_year):
            raise forms.ValidationError(_("Please select valid year."))        
        return news_date


