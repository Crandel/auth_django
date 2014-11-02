from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site
from ckeditor.fields import RichTextField

class HomeContents(models.Model):
    """
    Model for managing home page inner contents.
    """
    site = models.ForeignKey(Site,unique=True)
    main_itle = models.CharField(_('Main Title'), max_length=100,)
    sub_title = models.CharField(_('Sub Title'), max_length=100,)    
    ceo_title = models.CharField(_('CEO Title'), max_length=100,)
    ceo_desc = RichTextField(_('CEO Description'))
    

    def __unicode__(self):
        return self.main_itle

    class Meta:
        verbose_name = _('Home page content')
        verbose_name_plural = _('Home page contents')        


class HomeBanner(models.Model):
    """
    Model for managing home page banners.
    """
    home_content = models.ForeignKey(HomeContents,related_name='home_banner')
    banner_title = models.CharField(_('Banner Title'),max_length=100,null=True,blank=True)
    banner_link = models.URLField(_('Banner Link'),max_length=100,null=True,blank=True)
    banner_image = models.ImageField(_('Banner Image'),upload_to='banner/')
    sort_order = models.PositiveSmallIntegerField(_('Sort Order'), default=0)


    class Meta:
        verbose_name = _('Banner Image')
        verbose_name_plural = _('Banner Images')
        ordering = ('sort_order',)


class CEOImages(models.Model):
    """
    Model for managing CEO content in home page.
    """
    homecontent = models.ForeignKey(HomeContents,related_name='ceo_images')
    image_url = models.URLField(_('Image Url'),max_length=100,null=True,blank=True)
    ceo_image = models.ImageField(_('CEO Images'),upload_to='ceo/')
    sort_order = models.PositiveSmallIntegerField(_('Sort Order'), default=0)


    class Meta:
        verbose_name = _('CEO Image')
        verbose_name_plural = _('CEO Images')
        ordering = ('sort_order',)