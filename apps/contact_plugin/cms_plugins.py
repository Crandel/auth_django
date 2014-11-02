
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from models import ContactAddress
from modeltranslation.admin import TranslationAdmin

class ContactAddressPlugin(CMSPluginBase):
    """
    Plugin to render the contact address in contact page.
    """
    model = ContactAddress
    name = _("Contact Address Plugin")
    render_template = "contact_address.html"
    
    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

plugin_pool.register_plugin(ContactAddressPlugin)