from django.contrib.sites.models import Site
from django import template
from django.utils.translation import get_language

from cms.models.pagemodel import Page

from apps.general.models import FooterSettings,CommonSettings, BannerImages, TopMenuUrl
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
    return cms_pages

register.assignment_tag(cms_navigation)


def get_banners():
    banner = BannerImages.objects.filter(published=True)
    return banner
register.assignment_tag(get_banners)


def get_top_menu():
    menu = TopMenuUrl.objects.all()
    return menu
register.assignment_tag(get_top_menu)



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


def calculate_submenu(children):
    if children:
        main_menu = list()
        for page in children:
            if page.selected:
                main_menu.append({
                    'page': page,
                    'selected': True})
                sub_menu = [{
                    'page': page,
                    'selected': True
                }]
                for pg in page.children:
                    sub_menu.append({
                        'page': pg,
                        'selected': False})
            else:
                selected = False
                if page.children:
                    for pg in page.children:
                        if pg.selected:
                            selected = True
                            break
                if selected:
                    sub_menu = [{
                        'page': page,
                        'selected': False
                    }]
                    for pg in page.children:
                        sub_menu.append({
                            'page': pg,
                            'selected': pg.selected})
                main_menu.append({
                    'page': page,
                    'selected': selected})
        return {'main_menu': main_menu, 'sub_menu': sub_menu}
    return None

register.assignment_tag(calculate_submenu)


def calculate_submenu_our(children):
    if children:
        main_menu = list()
        for page in children:
            if page.selected:
                main_menu.append({
                    'page': page,
                    'selected': True})
                sub_menu = []
                for pg in page.children:
                    sub_menu.append({
                        'page': pg,
                        'selected': False})
            else:
                selected = False
                if page.children:
                    for pg in page.children:
                        if pg.selected:
                            selected = True
                            break
                if selected:
                    sub_menu = []
                    for pg in page.children:
                        sub_menu.append({
                            'page': pg,
                            'selected': pg.selected})
                main_menu.append({
                    'page': page,
                    'selected': selected})
        return {'main_menu': main_menu, 'sub_menu': sub_menu}
    return None

register.assignment_tag(calculate_submenu_our)


@register.filter
def search_include(result):
    try:
        template = result.object.search_template()
    except AttributeError:
        template = 'search/include/dummy.html'
    return template
