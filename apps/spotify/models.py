from django.db import models
import requests
from social_django.utils import load_strategy
# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=30, null=True)
    views = models.IntegerField(default=0, null=True)
    information = models.CharField(default='No Artist Information', max_length=200, null=True)

    def __str__(self):
        return self.name
    
    @classmethod
    def get_artist(cls):
        pass

class Song(models.Model):
    name = models.CharField(max_length=30, null=True)
    views = models.IntegerField(default=0, null=True)
    date = models.DateTimeField('Publication date', null=True)
    artist = models.ForeignKey( Artist, null=True,
                                 on_delete=models.CASCADE) # Eliminar un artista significa tmb eliminar toda su musica.

    def __str__(self):
        return self.name     # This allows us to see the name from the Django Admin interface
    
    @classmethod
    def get_song(cls):
        pass

class Spotify_User(models.Model):
    name = models.CharField(max_length=30, primary_key=True) # Spotify no tiene usuarios con el mismo nombre.
    access_token = models.CharField(max_length=200, null=True)
    refresh_token = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

    @classmethod
    def get_user(cls, request):     #Nos devuelve el usuario actual desde cualquier vista.
        if request.user.is_authenticated:
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
        else :
            exit()

class Playlist(models.Model):
    id = models.CharField(max_length=200, primary_key=True) # Es el id que tenga en Spotify
    name = models.CharField(max_length=30, null=True)
    duration = models.IntegerField(default=0, null=True)

    user = models.ForeignKey(Spotify_User, null=True,
                                on_delete=models.CASCADE)

    songs = models.ManyToManyField(Song)

    def __str__(self):
        return self.name

    def get_songs(self):
            pass

    @classmethod
    def get_playlist(cls, id, name, user):
        try:
            playlist = cls.objects.get(id = id)
        except cls.DoesNotExist:
            playlist = cls( id=id)
        playlist.name = name
        playlist.user = user
        playlist.save()
        return playlist
    
    @classmethod
    def get_playlists( cls, user):    #Get a List of a User's Playlists 
        response = requests.get(
            'https://api.spotify.com/v1/me/playlists',
            params={'access_token': user.access_token}
        )
        if response.status_code != 200:
            exit()
        playlists = response.json()["items"] # Array de diccionarios de cada playlist
        #elimina las playlist que no aparecen.
        playlists = []
        for playlist_json in playlists:
            id = playlist_json['id']
            name = playlist_json['name']
            playlists.append(cls.get_playlist( id=id, name=name, user=user))
        return playlists