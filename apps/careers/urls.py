from django.conf.urls import patterns, url
from apps.careers.views import CareerView, VacancyList, LoadMoreVacancy

urlpatterns = patterns(
    'apps.careers.views',
    url(r'^$', VacancyList.as_view(), name='vacancy_list'),
    url(r'^get-more/$', LoadMoreVacancy.as_view(), name='load_more_vac'),
    url(r'^job-vacancies/$', CareerView.as_view(), name='career'))
