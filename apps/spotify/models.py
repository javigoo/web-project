from django.db import models
import requests
from social_django.utils import load_strategy
# Create your models here.


class Artist(models.Model):
    id = models.CharField(max_length=200, primary_key=True) # Es el id que tenga en Spotify
    name = models.CharField(max_length=30, null=True)
    rate = models.IntegerField(default=0, null=True)
    information = models.CharField(default='No Artist Information', max_length=200, null=True)

    def __str__(self):
        return self.name
    
    @classmethod
    def get_artist(cls, id, name):
        try:
            artist = cls.objects.get(id = id)
        except cls.DoesNotExist:
            artist = cls( id=id)
        artist.id = id
        artist.name = name
        artist.save()
        return artist

class Song(models.Model):
    id = models.CharField(max_length=200, primary_key=True) # Es el id que tenga en Spotify
    name = models.CharField(max_length=30, null=True)
    rate = models.IntegerField(default=0, null=True)
    date = models.DateTimeField('Publication date', null=True)
    artist = models.ManyToManyField( Artist)

    def __str__(self):
        return self.name     # This allows us to see the name from the Django Admin interface
    
    def get_artists(self, artists):
        for artist in artists:
            id = artist['id']
            name = artist['name']
            Artist.get_artist( id=id, name=name)

    @classmethod
    def get_song(cls, artists, id, name, rate):
        try:
            song = cls.objects.get(id = id)
        except cls.DoesNotExist:
            song = cls( id=id)
        song.name = name
        song.rate = rate
        song.save()
        song.get_artists(artists=artists)
        return song

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
        playlists_dict = response.json()["items"] # Array de diccionarios de cada playlist
        #elimina las playlist que no aparecen.
        playlists_list = []
        for playlist_json in playlists_dict:
            id = playlist_json['id']
            name = playlist_json['name']
            playlists_list.append(cls.get_playlist( id=id, name=name, user=user))
        return playlists_list
    
    def get_songs(self):
        response = requests.get(
            'https://api.spotify.com/v1/playlists/'+self.id+'/tracks',
            params={'access_token': self.user.access_token}
        )
        if response.status_code != 200:
            exit()
        songs_dict = response.json()['items']
        songs_list = []
        for song_json in songs_dict:
            id = song_json['track']['id']
            artists = song_json['track']['artists']
            name = song_json['track']['name']
            rate = song_json['track']['popularity']
            song = Song.get_song(id=id, artists=artists, name=name, rate=rate)
            self.songs.add(song)
            songs_list.append(song)
        return songs_list