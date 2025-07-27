from django.db import models
from django.utils import timezone
import os
from uuid import uuid4


def video_upload_path(instance, file_name):
    extension = file_name.split('.')[-1]
    file_name = f"{uuid4().hex}.{extension}"
    return os.path.join('videos/', file_name)


def thumbnail_upload_path(instance, file_name):
    extension = file_name.split('.')[-1]
    file_name = f"{uuid4().hex}.{extension}"
    return os.path.join('thumbnails/', file_name)


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    video_file = models.FileField(upload_to=video_upload_path)
    thumbnail = models.ImageField(upload_to=thumbnail_upload_path, blank=True, null=True)

    def __str__(self):
        return self.title
