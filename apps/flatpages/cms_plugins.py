# To change this template, choose Tools | Templates
# and open the template in the editor.
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _
from apps.flatpages.models import HomeFlatPagePluginModel


class CMSHomeFlatPagePlugin(CMSPluginBase):
    model = HomeFlatPagePluginModel
    name = _("Flat page plugin")
    render_template = "flatpages/flatpage_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
            'placeholder': placeholder
        })
        return context

plugin_pool.register_plugin(CMSHomeFlatPagePlugin)
