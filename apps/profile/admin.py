from django.contrib import admin
from apps.profile.models import Profile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class ProfileAdmin(admin.StackedInline):
    model = Profile
    verbose_name_plural = 'Profile'


class UserAdmins(UserAdmin):
    inlines = (ProfileAdmin, )

admin.site.unregister(User)
admin.site.register(User, UserAdmins)
