from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': settings.MEDIA_ROOT,}),
    url(r'', include('django.contrib.staticfiles.urls')),

)

if settings.DEBUG:
    urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
)

admin.autodiscover()

urlpatterns += i18n_patterns('',
    url(r'^', include('apps.home.urls')),
    url(r'^kud-admin/', include(admin.site.urls)),
    (r'^ckeditor/', include('ckeditor.urls')),
    url(r'^contact-us/', include('apps.contactus.urls')),
    url(r'^news_events/', include('apps.newsevents.urls')),
    url(r'^career/', include('apps.careers.urls')),
    url(r'^portfolio/', include('apps.project.urls')),
    url(r'^kud-site/', include('apps.htmlsitemap.urls')),
    url(r'^', include('apps.xmlsitemap.urls')),
#    url(r'^search/', include('apps.search.urls')),
    (r'^search/', include('haystack.urls')),
    (r'^robots\.txt$', include('robots.urls')),
    url(r'^pages', include('django.contrib.flatpages.urls')),
    url(r'^', include('cms.urls')),
)


urlpatterns += patterns('',
        (r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )


