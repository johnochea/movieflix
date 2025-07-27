from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models
from django.utils import timezone
import os
from uuid import uuid4


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    '''
        This model represents the user profile.

        Fields:
        - email (email):        The user's email address
        - first_name (str):     The user's first name
        - last_name (str):      The user's last name
        - is_active (bool):     Indicates if the account is active
        - is_staff (bool):      Indicates if the user has admin privileges
    '''

    user = models.OneToOneField(
        'auth.User', on_delete=models.CASCADE, null=True, blank=True
    )
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.first_name + ' ' + self.last_name


def video_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid4().hex}.{ext}"
    return os.path.join('videos/', filename)


def thumbnail_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid4().hex}.{ext}"
    return os.path.join('thumbnails/', filename)


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    video_file = models.FileField(upload_to=video_upload_path)
    thumbnail = models.ImageField(upload_to=thumbnail_upload_path, blank=True, null=True)

    def __str__(self):
        return self.title
