from django.db import models
import requests

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
    id = models.AutoField(primary_key=True) #Ya lo usa Django por defecto.
    name = models.CharField(max_length=30, null=True)
    access_token = models.CharField(max_length=200, null=True)
    refresh_token = models.CharField(max_length=200, null=True)

    playlists = models.ManyToManyField('Playlist', related_name='Spotify_User')

    def __str__(self):
        return self.name

    @classmethod
    def get_user(cls, request):     #Nos devuelve el usuario actual desde cualquier vista.
        django_user = request.user #Usuario de django.contrib.auth users
        social = django_user.social_auth.get(provider='spotify') # Usuario de social_django
        try:
            app_user = cls.objects.get(name=social.uid) # Usuario de apps.spotify
        except cls.DoesNotExist:
            app_user = Spotify_User(name=social.uid)
        app_user.access_token = social.extra_data["access_token"]
        app_user.refresh_token = social.extra_data["refresh_token"]
        app_user.save()
        return app_user
    
    """def get_playlist(self):    #Get a List of a User's Playlists 
        response = requests.get(
            'https://api.spotify.com/v1/users/'+self.name+'/playlists',
            params={'access_token': self.access_token}
        )
        playlists = response.json()['items']
        self.playlists.set() = playlists{'traks'}
        user.save()
"""