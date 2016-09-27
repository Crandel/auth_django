import logging
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.core import validators
from django.utils.translation import ugettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField

logger = logging.getLogger(__name__)
AbstractUser._meta.get_field('email')._unique = True
AbstractUser._meta.get_field('email').blank = False
AbstractUser._meta.get_field('username')._unique = True
AbstractUser._meta.get_field('username').validators = [validators.RegexValidator(r'^[\w\W\ .@+-]+$',
                                      _('Enter a valid username. '
                                        'This value may contain only letters, numbers '
                                        'and @/./+/-/ /_ characters.'), 'invalid')]


class User(AbstractUser):
    twitter = models.CharField(_('Tweeter'), max_length=255, null=True)
    facebook = models.CharField(_('Facebook'), max_length=255, null=True)
    google = models.CharField(_('Google+'), max_length=255, null=True)
    vk = models.CharField(_('Vkontakte'), max_length=255, null=True)
    avatar = models.ImageField(_('Avatar'), max_length=255, upload_to="user", null=True, blank=True)
    authentication_hash = models.CharField(_('hash'), max_length=255)
    address = models.CharField(_('Address'), max_length=255, null=True)
    phone = PhoneNumberField(blank=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('activate', kwargs={'key': self.authentication_hash})
