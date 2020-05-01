from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from apps.spotify.models import *
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import redirect

from rest_framework import viewsets
from apps.spotify.serializers import UserSerializer

# Create your views here.
def home(request):
        return render(request, 'spotify/home.html', {})

def top_songs(request):
    try:
        top = Song.objects.order_by('rate').reverse()[:10]  # Top 10 songs by views (rate)
    except len(top)==0:
        raise Http404("Error, there are no songs available.")
    return render(request, 'spotify/topsongs.html', {'topsonglist':top})

def playlist_view(request):
    user = Spotify_User.get_user(request)
    playlists = Playlist.get_playlists(user)
    return render(request, 'spotify/playlists.html', {'playlist_list':playlists})

def profile(request):
    app_user = Spotify_User.get_user(request)
    return render(request, 'spotify/profile.html', {'usuario':app_user})

def log_out(request):
    logout(request)
    return render(request, 'spotify/logout.html', {})   # Redirect to a success page.

def infoplaylist(request, playlist_id):
    playlist = Playlist.objects.get(id=playlist_id)
    songs = playlist.get_songs()
    return render(request, 'spotify/infoplaylist.html', {'song_list':songs, 'playlist':playlist.name})

def artist_view(request):
    try:
        artists = Artist.objects.all()
    except len(artists)==0:
        raise Http404("Error, no artist information available.")
    return render(request, 'spotify/artists.html', {'artistlist':artists})

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer