from django.test import TestCase
from django.core.urlresolvers import reverse

from apps.profile.models import Profile


class ProfileTestCase(TestCase):
    fixtures = ['apps/fixtures/test_profiles.json']

    def test_profile(self):
        self.profile = Profile.objects.get(pk=1)
        self.assertEqual(self.profile.google, 'google')
        self.assertEqual(self.profile.facebook, 'facebook')
        self.assertEqual(self.profile.twitter, 'twitter')
        self.assertEqual(self.profile.vk, 'vk')
        self.assertEqual(self.profile.address, 'address')
        self.assertEqual(self.profile.phone.national_number, 977777777)

    def test_url(self):
        self.assertEqual(self.client.get(reverse('login')).status_code, 200)
        self.assertEqual(self.client.get(reverse('sign')).status_code, 200)
        self.assertEqual(self.client.get(reverse('success')).status_code, 200)
