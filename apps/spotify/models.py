from django.db import models


# Create your models here.


class Artist(models.Model):
    id = models.CharField(max_length=200, primary_key=True)  # Spotify id
    name = models.CharField(max_length=30, null=True)
    rate = models.IntegerField(default=0, null=True)
    information = models.CharField(default='No Artist Information', max_length=200, null=True)

    def __str__(self):
        return self.name

    @classmethod
    def get_artist(cls, id, name):
        try:
            artist = cls.objects.get(id=id)
        except cls.DoesNotExist:
            artist = cls(id=id)
        artist.id = id
        artist.name = name
        artist.save()
        return artist


class Song(models.Model):
    id = models.CharField(max_length=200, primary_key=True)  # Spotify id
    name = models.CharField(max_length=30, null=True)
    rate = models.IntegerField(default=0, null=True)
    date = models.DateTimeField('Publication date', null=True)
    artist = models.ManyToManyField(Artist)

    def __str__(self):
        return self.name  # This allows us to see the name from the Django Admin interface

    def get_artists(self, artists):
        for artist in artists:
            id = artist['id']
            name = artist['name']
            Artist.get_artist(id=id, name=name)

    @classmethod
    def get_song(cls, artists, id, name, rate):
        try:
            song = cls.objects.get(id=id)
        except cls.DoesNotExist:
            song = cls(id=id)
        song.name = name
        song.rate = rate
        song.save()
        song.get_artists(artists=artists)
        return song


class Spotify_User(models.Model):
    name = models.CharField(max_length=30,
                            primary_key=True)  # Primary key because Spotify has no members with the same name.
    access_token = models.CharField(max_length=200, null=True)
    refresh_token = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Playlist(models.Model):
    id = models.CharField(max_length=200, primary_key=True)  # Spotify id
    name = models.CharField(max_length=30, null=True)
    duration = models.IntegerField(default=0, null=True)

    user = models.ForeignKey(Spotify_User, null=True,
                             on_delete=models.CASCADE)

    songs = models.ManyToManyField(Song)

    is_local = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    @classmethod
    def get_playlist(cls, id, name, user):
        try:
            playlist = cls.objects.get(id=id)
        except cls.DoesNotExist:
            playlist = cls(id=id)
        playlist.name = name
        playlist.user = user
        playlist.save()
        return playlist
