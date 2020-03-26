from django.db import models
import requests
from social_django.utils import load_strategy

# Create your models here.

class Song(models.Model):
    name = models.CharField(max_length=30, null=True)
    views = models.IntegerField(default=0, null=True)
    date = models.DateTimeField('Publication date', null=True)

    #song = models.ForeignKey(Song, null=True, on_delete= models.SET_NULL)

    def __str__(self):
        return self.name     # This allows us to see the name from the Django Admin interface
    
    @classmethod
    def get_song(cls):
        pass

class Artist(models.Model):
    name = models.CharField(max_length=30, null=True)
    views = models.IntegerField(default=0, null=True)
    information = models.CharField(default='No Artist Information', max_length=200, null=True)

    songs = models.ManyToManyField('Song', related_name='Artist')   # We can access Song.Artist to give us a list of songs from that artist

    def __str__(self):
        return self.name
    
    @classmethod
    def get_artist(cls):
        pass

class Playlist(models.Model):
    id = models.CharField(max_length=200, primary_key=True) # Es el id que tenga en Spotify
    name = models.CharField(max_length=30, null=True)
    duration = models.IntegerField(default=0, null=True)

    songs = models.ManyToManyField(Song)

    def __str__(self):
        return self.name

    @classmethod
    def get_playlist(cls, id, name):
        try:
            playlist = cls.objects.get(id = id)
        except cls.DoesNotExist:
            playlist = cls( id=id)
        playlist.name = name
        playlist.save()
        return playlist
    
    def get_songs(self):
        pass

class Spotify_User(models.Model):
    name = models.CharField(max_length=30, primary_key=True) # Spotify no tiene usuarios con el mismo nombre.
    access_token = models.CharField(max_length=200, null=True)
    refresh_token = models.CharField(max_length=200, null=True)

    playlists = models.ManyToManyField( Playlist, related_name='Spotify_User')

    def __str__(self):
        return self.name

    @classmethod
    def get_user(cls, request):     #Nos devuelve el usuario actual desde cualquier vista.
        try:
            django_user = request.user #Usuario de django.contrib.auth users
            social = django_user.social_auth.get(provider='spotify') # Usuario de social_django
            try:
                app_user = cls.objects.get(name=social.uid) # Usuario de apps.spotify
            except cls.DoesNotExist:
                app_user = cls(name=social.uid)
            
            app_user.access_token = social.get_access_token(load_strategy()) # En caso de ser necesario, actualiza el access token
            app_user.refresh_token = social.extra_data["refresh_token"]
            app_user.save()
            return app_user
        except not request.user.is_authenticated:
            exit()
    
    def get_playlists(self):    #Get a List of a User's Playlists 
        response = requests.get(
            'https://api.spotify.com/v1/me/playlists',
            params={'access_token': self.access_token}
        )
        if response.status_code != 200:
            exit()
        playlists = response.json()["items"] # Array de diccionarios de cada playlist
        #self.playlists.purgue()
        for playlist_json in playlists:
            id = playlist_json['id']
            name = playlist_json['name']
            playlist = Playlist.get_playlist( id=id, name=name)
            self.playlists.add(playlist)
        self.save()
        return self.playlists