from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
import models
from modeltranslation.admin import TranslationAdmin

import admin
class CMSGalleryPlugin(CMSPluginBase):

    model = models.GalleryPluginModel
    inlines = [admin.ImageInline, ]
    name = _('Image gallery')
    render_template = 'gallery.html'

    def render(self, context, instance, placeholder):
        context.update({
                        'images': instance.gallery_images.all(),
                        'gallery': instance,
                       })
        
        return context

plugin_pool.register_plugin(CMSGalleryPlugin)