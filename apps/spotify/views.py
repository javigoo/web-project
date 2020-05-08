import requests
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, redirect
from social_django.utils import load_strategy

from apps.spotify.forms import PlaylistForm
from apps.spotify.models import *

# Create your views here.
def home(request):
    return render(request, 'spotify/home.html', {})


def top_songs(request):
    try:
        top = Song.objects.order_by('rate').reverse()[:10]  # Top 10 songs by views (rate)
    except len(top) == 0:
        raise Http404("Error, there are no songs available.")
    return render(request, 'spotify/topsongs.html', {'topsonglist': top})


def playlist_view(request):
    user = get_user(request)
    playlists = get_playlists(user)
    return render(request, 'spotify/playlists.html', {'playlist_list': playlists})


def profile(request):
    app_user = get_user(request)
    return render(request, 'spotify/profile.html', {'usuario': app_user})


def log_out(request):
    logout(request)
    return render(request, 'spotify/logout.html', {})  # Redirect to a success page.


def infoplaylist(request, playlist_id):
    playlist = Playlist.objects.get(id=playlist_id)
    songs = get_songs(playlist)
    return render(request, 'spotify/infoplaylist.html', {'song_list': songs, 'playlist': playlist.name})


def artist_view(request):
    try:
        artists = Artist.objects.all()
    except len(artists) == 0:
        raise Http404("Error, no artist information available.")
    return render(request, 'spotify/artists.html', {'artistlist': artists})


def create_playlist(request):
    form = PlaylistForm()
    if request.method == 'POST':
        #print('Printing post:', request.POST)
        form = PlaylistForm(request.POST)
        if form.is_valid():
            form.save()     # Aqui deberiamos conectarnos con la api de spoti y crear la nueva playlist
            return redirect('/')

    context = {'form': form}
    return render(request, 'spotify/form.html', context)


# API Queries


def get_user(request):  # Returns the current user from any view.
    if request.user.is_authenticated:
        django_user = request.user  # Django.contrib.auth users
        social = django_user.social_auth.get(provider='spotify')  # User of social_django
        try:
            app_user = Spotify_User.objects.get(name=social.uid)  # Apps.spotify user
        except Spotify_User.DoesNotExist:
            app_user = Spotify_User(name=social.uid)

        app_user.access_token = social.get_access_token(
            load_strategy())  # If necessary, the access token is updated
        app_user.refresh_token = social.extra_data["refresh_token"]
        app_user.save()
        return app_user
    else:
        exit()


def get_playlists(user):  # Get a List of a User's Playlists

    response = requests.get(
        'https://api.spotify.com/v1/me/playlists',
        params={'access_token': user.access_token}
    )
    if response.status_code != 200:
        exit()
    playlists_dict = response.json()["items"]  # Array of dictionaries for each playlist
    playlists_list = []  # Remove playlists that do not appear.
    for playlist_json in playlists_dict:
        id = playlist_json['id']
        name = playlist_json['name']
        playlists_list.append(Playlist.get_playlist(id=id, name=name, user=user))

    for playlist in Playlist.objects.filter(user=user):     # Añade las playlist creadas a traves de Spotifly
        playlists_list.append(playlist)

    return playlists_list


def get_songs(self):
    response = requests.get('https://api.spotify.com/v1/playlists/' + self.id + '/tracks',
                            params={'access_token': self.user.access_token})
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