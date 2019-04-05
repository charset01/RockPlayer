from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Album(models.Model):
    name = models.CharField(max_length=35)
    artist = models.CharField(max_length=45)
    album_genre = models.CharField(max_length=45)
    album_cover = models.FileField()
    def get_absolute_url(self):
        return reverse('RockPlayer:index')

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_name = models.CharField(max_length=25)
    song_audio = models.FileField()

    def get_absolute_url(self):
        return reverse('RockPlayer:detail')

