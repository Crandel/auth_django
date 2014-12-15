from __future__ import unicode_literals
from requests import request, HTTPError, get
import hashlib
from datetime import datetime

from django.conf import settings

from apps.profile.models import Profile


def save_profile(backend, user, response, is_new=False, *args, **kwargs):

    if backend.name == 'facebook':

        uid = response['id']

        if is_new:
            url = 'http://graph.facebook.com/{0}/picture'.format(uid)
            try:
                responses = request('GET', url, params={'type': 'large'})

                hashing = hashlib.sha224(str(datetime.now())).hexdigest()
                url_photo = save_profile_photo(responses.url, uid)
                profile = Profile.objects.create(
                    user=user, authentication_hash=hashing, profile_photo=url_photo, facebook=uid
                )
                profile.save()
                responses.raise_for_status()
            except HTTPError:
                pass
        else:
            profile = Profile.objects.get(user=user)
            if not profile.profile_photo:
                url = 'http://graph.facebook.com/{0}/picture'.format(uid)
                try:
                    responses = request('GET', url, params={'type': 'large'})
                    url_photo = save_profile_photo(responses.url, uid)
                    profile.profile_photo = url_photo
                    profile.save()
                    responses.raise_for_status()
                except HTTPError:
                    pass

            if not profile.facebook:
                profile.facebook = uid
                profile.save()

    if backend.name == 'twitter':

        uid = response['id']

        if is_new:
            hashing = hashlib.sha224(str(datetime.now())).hexdigest()
            profile = Profile.objects.create(
                user=user, authentication_hash=hashing,
                profile_photo=save_profile_photo(response['profile_image_url_https'], uid), twitter=uid
            )
            profile.save()
        else:
            profile = Profile.objects.get(user=user)
            if not profile.profile_photo:

                profile.profile_photo = save_profile_photo(response['profile_image_url_https'], uid)

            if not profile.twitter:
                profile.twitter = uid

            profile.save()

    if backend.name == 'google-oauth2':

        uid = response['id']

        if is_new:
            hashing = hashlib.sha224(str(datetime.now())).hexdigest()

            profile = Profile.objects.create(
                user=user, authentication_hash=hashing,
                profile_photo=save_profile_photo(response['image']['url'], uid), google=uid
            )
            profile.save()
        else:
            profile = Profile.objects.get(user=user)
            if not profile.profile_photo:
                profile.profile_photo = save_profile_photo(response['image']['url'], uid)

            if not profile.google:
                profile.google = uid

            profile.save()

    if backend.name == 'vk-oauth2':

        uid = response['uid']

        if is_new:
            hashing = hashlib.sha224(str(datetime.now())).hexdigest()

            profile = Profile.objects.create(
                user=user, authentication_hash=hashing, profile_photo=save_profile_photo(response['user_photo'], uid), vk=uid
            )
            profile.save()
        else:
            profile = Profile.objects.get(user=user)
            if not profile.profile_photo:
                profile.profile_photo = save_profile_photo(response['user_photo'], uid)

            if not profile.vk:
                profile.vk = uid

            profile.save()


def save_profile_photo(url, uid):
    photo = get(url)

    photo_name = "profile/{0}.jpg".format(str(uid))

    out = open(settings.MEDIA_ROOT + "/" + photo_name, 'wb')
    out.write(photo.content)
    out.close()

    return photo_name