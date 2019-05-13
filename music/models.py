from django.db import models

# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.CharField(max_length=255)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    artists = models.ManyToManyField(Artist)
    released = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name