from django.contrib.sites.models import Site
from django import template
from django.utils.translation import get_language

from cms.models.pagemodel import Page

from apps.general.models import FooterSettings,CommonSettings, BannerImages
from apps.flatpages.models import FlatPage

register = template.Library()

def footerset():
    """
    Template tags for getting footer contents.
    """
    footer_settings=None
    try:
        current_site = Site.objects.get_current()
        footer_settings = FooterSettings.objects.get(site=current_site)
    except:
        pass
    return footer_settings
register.assignment_tag(footerset)

def get_logo():
    """
    Template tags for getting logo.
    """
    common=None
    try:
        current_site = Site.objects.get_current()
        common = CommonSettings.objects.get(site=current_site)
    except:
        pass
    return common
register.assignment_tag(get_logo)


def cms_navigation():
    cms_pages = Page.objects.filter(in_navigation=True, parent_id__isnull=True).distinct()
    for page in cms_pages:
        print page.pk
    return cms_pages

register.assignment_tag(cms_navigation)


def get_banners():
    banner = BannerImages.objects.filter(published=True)
    return banner
register.assignment_tag(get_banners)


@register.filter
def get_other_language_path(path):
    lan = get_language()
    if lan=='en':
        return path.replace('/en/','/ar/')
    return path.replace('/ar/','/en/')


def get_flatpage(page_type):
    if page_type == 'about':
        try:
            current_site = Site.objects.get_current()
            about_us = FlatPage.objects.filter(select_link='about')
        except:
            pass
        if about_us:
            return about_us
    elif page_type == 'footer':
        try:
            current_site = Site.objects.get_current()
            footer = FlatPage.objects.filter(select_link='footer')
        except:
            pass
        if footer:
            return footer
register.assignment_tag(get_flatpage)


@register.filter
def partition(thelist, n):
    try:
        n = int(n)
        thelist = list(thelist)
    except (ValueError, TypeError):
        return [thelist]
    p = len(thelist) / n
    return [thelist[p*i:p*(i+1)] for i in range(n - 1)] + [thelist[p*(i+1):]]
