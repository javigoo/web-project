from django.db import models

# Create your models here.

class Song(models.Model):
    name = models.CharField(max_length=30, null=True)
    views = models.IntegerField(default=0, null=True)
    date = models.DateTimeField('Publication date', null=True)

    #song = models.ForeignKey(Song, null=True, on_delete= models.SET_NULL)

    def __str__(self):
        return self.name     # This allows us to see the name from the Django Admin interface

class Artist(models.Model):
    name = models.CharField(max_length=30, null=True)
    views = models.IntegerField(default=0, null=True)
    information = models.CharField(default='No Artist Information', max_length=200, null=True)

    songs = models.ManyToManyField('Song', related_name='Artist')   # We can access Song.Artist to give us a list of songs from that artist

    def __str__(self):
        return self.name

class Playlist(models.Model):
    name = models.CharField(max_length=30, null=True)
    duration = models.IntegerField(default=0, null=True)

    song = models.ManyToManyField(Song)

    def __str__(self):
        return self.name

class Spotify_User(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=30, null=True)

    playlists = models.ManyToManyField('Playlist', related_name='Spotify_User')

    def __str__(self):
        return self.name
