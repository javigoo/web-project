from django.db import models

# Create your models here.

class Song(models.Model):
    name = models.CharField(max_length=200, null=True)
    views = models.IntegerField(default=0, null=True)
    date = models.DateTimeField('date published', null=True)

    #song = models.ForeignKey(Song, null=True, on_delete= models.SET_NULL)

    def __str__(self):
        return self.name     # Esto nos permite ver el nombre desde Django Administration

class Artist(models.Model):
    name = models.CharField(max_length=200, null=True)
    views = models.IntegerField(default=0, null=True)
    information = models.CharField(default='No Artist Information', max_length=200, null=True)

    song = models.ManyToManyField(Song)

    def __str__(self):
        return self.name

class Playlist(models.Model):
    name = models.CharField(max_length=200, null=True)
    duration = models.IntegerField(default=0, null=True)

    song = models.ManyToManyField(Song)

    def __str__(self):
        return self.name
