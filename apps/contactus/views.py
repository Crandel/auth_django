from django.views.generic.edit import FormView
from django.contrib.sites.models import Site
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _

from apps.contactus.forms import ContactUsForm
from apps.contactus.models import GoogleContact

class ContactView(FormView):
    template_name = 'contactus/contact.html'
    form_class = ContactUsForm
    success_url = '/contact-us/'

    """
    Customized form view for provide contact
    form to get the contact details from the end user.
    """

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        form.send_mail()
        messages.info( self.request,_('Thanks for contacting us.We will contact you soon!'))
        return super(ContactView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        current_site = Site.objects.get_current() 
        context['google_cordinates'] = GoogleContact.objects.get(site = current_site)
        return context


