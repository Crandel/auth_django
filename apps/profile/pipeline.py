from __future__ import unicode_literals
from requests import request, HTTPError
import hashlib
from datetime import datetime

from apps.profile.models import Profile


def save_profile(backend, user, response, is_new=False, *args, **kwargs):
    print(backend.name, 123, is_new)
    if is_new and backend.name == 'facebook':
        url = 'http://graph.facebook.com/{0}/picture'.format(response['id'])
        try:
            responses = request('GET', url, params={'type': 'large'})

            hashing = hashlib.sha224(str(datetime.now())).hexdigest()
            profile = Profile.objects.create(
                user=user, autentification_hash=hashing, profile_photo=responses.url, facebook=response['id']
            )
            profile.save()
            responses.raise_for_status()
        except HTTPError:
            pass

    if is_new and backend.name == 'twitter':
        hashing = hashlib.sha224(str(datetime.now())).hexdigest()
        profile = Profile.objects.create(
            user=user, autentification_hash=hashing, profile_photo=response['profile_image_url_https'], twitter=response['id']
        )
        profile.save()
