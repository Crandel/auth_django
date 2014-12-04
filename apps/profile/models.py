from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _


class Profile(models.Model):
    user = models.OneToOneField(User)
    twitter = models.CharField(_('Tweeter'), max_length=255, null=True)
    facebook = models.CharField(_('Facebook'), max_length=255, null=True)
    profile_photo = models.ImageField(_('Photo'), max_length=255, upload_to="profile", null=True)
    autentification_hash = models.CharField(_('hash'), max_length=255)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Contact Us')

    def get_absolute_url(self):
        return reverse('activate', kwargs={'key': self.autentification_hash})
