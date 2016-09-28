# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views import defaults as default_views
from django.utils.translation import ugettext_lazy as _

# Text to put at the end of each page's <title>.
admin.site.site_title = _('Auth admin page')

# Text to put in each page's <h1> (and above login form).
admin.site.site_header = _('Auth administration')

# Text to put at the top of the admin index page.
admin.site.index_title = _('Auth administration')

urlpatterns = [
    url(r'^', include('users.urls')),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request),
        url(r'^403/$', default_views.permission_denied),
        url(r'^404/$', default_views.page_not_found),
        url(r'^500/$', default_views.server_error),
    ]
