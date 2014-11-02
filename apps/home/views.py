from django.views.generic.base import TemplateView
from django.contrib.sites.models import Site
from django.utils.translation import get_language


from apps.newsevents.models import News
from apps.home.models import *




class HomePageView(TemplateView):
    template_name = "home.html"
    """
    Customized template view to manage content of home page.
    """
    
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        image_list = []
        try:
            current_site = Site.objects.get_current()
            news = News.objects.filter(site = current_site).filter(is_published=True)[:6]
            home_contents = HomeContents.objects.get(site = current_site)
            for content in home_contents.ceo_images.all():
                image_list.append(content)
        except:
            pass
        context['image_list'] = reversed(image_list)
        context['home_contents']=home_contents
        context['news'] = news        
        return context