from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = i18n_patterns('',
    url(r'^kud-admin/', include(admin.site.urls)),
    (r'^ckeditor/', include('ckeditor.urls')),
    url(r'^contact-us/', include('apps.contactus.urls')),
    url(r'^portfolio/', include('apps.portfolio.urls')),
    url(r'^career/', include('apps.careers.urls')),
    url(r'^kud-site/', include('apps.htmlsitemap.urls')),
    url(r'^sitemap/', TemplateView.as_view(template_name="sitemap/sitemap.html"), name="site_map"),
    url(r'^', include('apps.xmlsitemap.urls')),
    # url(r'^search/', include('apps.search.urls')),
    (r'^search/', include('haystack.urls')),
    (r'^robots\.txt$', include('robots.urls')),
    url(r'^pages', include('django.contrib.flatpages.urls')),
    url(r'^', include('cms.urls')),
)

urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': settings.MEDIA_ROOT,}),
    url(r'', include('django.contrib.staticfiles.urls')),

) + urlpatterns

if settings.DEBUG:
    urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
)

urlpatterns += patterns('',
        (r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )


