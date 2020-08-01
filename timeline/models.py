import datetime
from pathlib import Path

import filetype
from django.db import models

TEXT_SHORT = 25
SMALL_TEXT = 256
LARGE_TEXT = 1500


# Create your models here.
class Moment(models.Model):
    title = models.CharField(max_length=SMALL_TEXT)
    description = models.CharField(max_length=LARGE_TEXT, blank=True, )
    timestamp = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.title

    def get_gallery(self):
        return self.gallery.get_queryset()


def moment_gallery_path(instance, filename):
    return Path('timeline') / str(instance.moment) / filename


class Media(models.Model):
    moment = models.ForeignKey(Moment, related_name='gallery', on_delete=models.CASCADE)
    file = models.FileField(upload_to=moment_gallery_path)
    TYPE_CHOICES = (
        ('i', 'Image'),
        ('v', 'Video'),
    )
    type = models.CharField(max_length=TEXT_SHORT, choices=TYPE_CHOICES)

    class Meta:
        verbose_name_plural = 'Media'

    def __str__(self):
        return f'{self.moment}:{self.file.name}'

    def save(self, *args, **kwargs):
        file_mime = filetype.guess_mime(self.file).lower()
        if 'video' in file_mime:
            self.type = 'v'
        elif 'image' in file_mime:
            self.type = 'i'
        else:
            # Should raise eror
            raise TypeError("Media file not supported or invalid.")
        super(Media, self).save(*args, **kwargs)
