from django.conf.urls import url

from apps.profile import views


urlpatterns = [
    url(r'^$', views.MainView.as_view(), name='main'),
    url(r'^sign/$', views.SignView.as_view(), name='sign'),
    url(r'^activate/(?P<key>[\w-]+)/$', views.ActivateView.as_view(), name='activate'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^success/$', views.SuccessView.as_view(), name='success'),
    url(r'^user/(?P<pk>[\d-]+)/$', views.ChangeUserView.as_view(), name='change_user'),
    url(r'^profile/(?P<pk>[\d-]+)/$', views.ChangeProfileView.as_view(), name='change_profile'),
]
