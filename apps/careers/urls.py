from django.conf.urls import patterns, url
from apps.careers.views import VacancyList, LoadMoreVacancy, SendCV, VacancyApplyView, SelectNationality

urlpatterns = patterns(
    'apps.careers.views',
    url(r'^$', VacancyList.as_view(), name='vacancy_list'),
    url(r'^get-more/$', LoadMoreVacancy.as_view(), name='load_more_vac'),
    url(r'^send-cv/$', SendCV.as_view(), name='send_cv'),
    url(r'^sel-nat/$', SelectNationality.as_view(), name='select_nat'),
    url(r'^apply/(?P<pk>\d+)/$', VacancyApplyView.as_view(), name='vacancy_apply'),)
