from __future__ import unicode_literals
from requests import request, HTTPError
import hashlib
from datetime import datetime

from apps.profile.models import Profile


def save_profile(backend, user, response, is_new=False, *args, **kwargs):

    if backend.name == 'facebook':

        if is_new:
            url = 'http://graph.facebook.com/{0}/picture'.format(response['id'])
            try:
                responses = request('GET', url, params={'type': 'large'})

                hashing = hashlib.sha224(str(datetime.now())).hexdigest()
                profile = Profile.objects.create(
                    user=user, authentication_hash=hashing, profile_photo=responses.url, facebook=response['id']
                )
                profile.save()
                responses.raise_for_status()
            except HTTPError:
                pass
        else:
            profile = Profile.objects.get(user=user)
            if not profile.profile_photo:
                url = 'http://graph.facebook.com/{0}/picture'.format(response['id'])
                try:
                    responses = request('GET', url, params={'type': 'large'})
                    profile.profile_photo = responses.url
                    profile.save()
                    responses.raise_for_status()
                except HTTPError:
                    pass

            if not profile.facebook:
                profile.facebook = response['id']
                profile.save()

    if backend.name == 'twitter':

        if is_new:
            hashing = hashlib.sha224(str(datetime.now())).hexdigest()
            profile = Profile.objects.create(
                user=user, authentication_hash=hashing, profile_photo=response['profile_image_url_https'], twitter=response['id']
            )
            profile.save()
        else:
            profile = Profile.objects.get(user=user)
            if not profile.profile_photo:
                profile.profile_photo = response['profile_image_url_https']

            if not profile.twitter:
                profile.twitter = response['id']

            profile.save()

    if backend.name == 'google-oauth2':

        if is_new:
            hashing = hashlib.sha224(str(datetime.now())).hexdigest()
            profile = Profile.objects.create(
                user=user, authentication_hash=hashing, profile_photo=response['image']['url'], google=response['id']
            )
            profile.save()
        else:
            profile = Profile.objects.get(user=user)
            if not profile.profile_photo:
                profile.profile_photo = response['image']['url']

            if not profile.google:
                profile.google = response['id']

            profile.save()

    if backend.name == 'vk-oauth2':

        if is_new:
            hashing = hashlib.sha224(str(datetime.now())).hexdigest()
            profile = Profile.objects.create(
                user=user, authentication_hash=hashing, profile_photo=response['user_photo'], vk=response['uid']
            )
            profile.save()
        else:
            profile = Profile.objects.get(user=user)
            if not profile.profile_photo:
                profile.profile_photo = response['user_photo']

            if not profile.vk:
                profile.vk = response['uid']

            profile.save()