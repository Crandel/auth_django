from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField

class GalleryPluginModel(CMSPlugin):
    title = models.CharField(_('Title'),max_length=50)
    desc = RichTextField(_('Description'))
    image = models.ImageField(_('Main Image'),upload_to='cms_gallery_img/')
    def copy_relations(self, oldinstance):
        for gallery_image in oldinstance.gallery_images.all():
            # instance.pk = None; instance.pk.save() is the slightly odd but
            # standard Django way of copying a saved model instance
            gallery_image.pk = None
            gallery_image.plugin = self            
            gallery_image.save()

class GalleryImage(models.Model):
    plugin = models.ForeignKey(
        GalleryPluginModel,
        related_name="gallery_images"
        )
    image = models.ImageField(_('Gallery Image'),upload_to='cms_gallery_img/')

    sort_order = models.PositiveSmallIntegerField(_('Sort Order'),default=0)

    class Meta:
        ordering = ('sort_order',)