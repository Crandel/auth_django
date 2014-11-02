
from django.views.generic.base import TemplateView
from django.db.models import Q
from cms.models import Title
from apps.newsevents.models import Events

class SearchView(TemplateView):
    template_name = "search/search.html"
    """
    Customized template view to manage content of search page.
    """
    def get_context_data(self,**kwargs):
        results = []
        q = self.request.GET.get('q')
        if q:
            print "qqqqqqqqqqqq",q
            cms_pages = Title.objects.filter(Q(title__icontains=q))            
            for title_content in cms_pages:
                results.append(('',title_content.title))

            try:
                events = Events.objects.filter(Q(event_title__icontains=q))
                for event in events:
                    results.append((event.event_title_en,event.event_title_ar,event.event_desc_en,event.event_desc_ar))
            except:
                pass
        print results
        context = super(SearchView, self).get_context_data(**kwargs)
        context['results'] = results
        return context