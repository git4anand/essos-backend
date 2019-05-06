from django.db import models
from music.models import Song


class Playlist(models.Model):
    name = models.CharField(max_length=255)
    songs = models.ManyToManyField(Song, blank=True)

    def __str__(self):
        return self.name