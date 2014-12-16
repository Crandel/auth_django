from __future__ import unicode_literals
from webtest import Upload

from django.core import mail
from django_webtest import WebTest
from django.test import TestCase
from django.conf import settings
from django.core.urlresolvers import reverse

from apps.profile.models import Profile


class ProfileTestCase(TestCase):
    fixtures = ['apps/fixtures/test_profiles.json', 'apps/fixtures/test_user.json']

    def test_profile(self):
        self.profile = Profile.objects.get(pk=1)
        self.assertEqual(self.profile.google, 'google')
        self.assertEqual(self.profile.facebook, 'facebook')
        self.assertEqual(self.profile.twitter, 'twitter')
        self.assertEqual(self.profile.vk, 'vk')
        self.assertEqual(self.profile.address, 'address')
        self.assertEqual(self.profile.phone.national_number, 977777777)
        self.assertEqual(self.profile.user.username, 'crandel')

    def test_url(self):
        self.assertEqual(self.client.get(reverse('login')).status_code, 200)
        self.assertEqual(self.client.get(reverse('sign')).status_code, 200)
        self.assertEqual(self.client.get(reverse('success')).status_code, 200)

    def test_registration(self):
        self.assertTrue(True)


class RegistrationTest(WebTest):
    fixtures = ['apps/fixtures/test_profiles.json', 'apps/fixtures/test_user.json']

    def testLoginAndLogout(self):
        form = self.app.get(reverse('login')).form
        form['username'] = 'crandel'
        form['password'] = 'metalist20'
        response = form.submit().follow()
        self.assertEqual(response.context['user'].username, 'crandel')
        page = self.app.get(reverse('logout'), user='crandel')
        assert 'login' in page['Location']

    def testChangeProfile(self):
        user_page = self.app.get(reverse('change_user', kwargs={'pk': 1}), user='crandel').form
        user_page['username'] = 'second'
        user_page['email'] = 'drevenchuk@steelkiwi.com'
        user_page['first_name'] = 'vetal'
        user_page['last_name'] = 'last_name'
        profile_form = user_page.submit().follow().form
        profile_form['phone'] = '+380977370429'
        profile_form['address'] = 'new_address'
        profile_form['profile_photo'] = Upload('test.png', open(settings.BASE_DIR+'/test.png').read())
        profile_form.submit().follow()
        confirm = self.app.get(reverse('main'))
        self.assertEqual(confirm.context['user'].username, 'second')
