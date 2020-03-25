from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from apps.spotify.models import *
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import redirect
import requests

# Create your views here.
def home(request):
    #if request.user.is_authenticated:
        return render(request, 'spotify/home.html', {})
    #else:
    #    raise Http404

def top_songs(request):
    try:
        lista = Song.objects.order_by('views').reverse()[:10] #Top 10 Songs by views
    except len(lista)==0:
        raise Http404("Error, lista vacia.")
    return render(request, 'spotify/topsongs.html', {'topsonglist':lista})

def playlist_view(request):
    try:
        playlists = Playlist.objects.all()
    except len(lista)==0:
        raise Http404("Error, lista vacia.")
    return render(request, 'spotify/playlists.html', {'playlist_list':playlists})

def profile(request):
    django_user = request.user #Usuario de django.contrib.auth users
    social = django_user.social_auth.get(provider='spotify') # Usuario de social_django
    try:
        app_user = Spotify_User.objects.get(name=social.uid) # Usuario de apps.spotify
    except Spotify_User.DoesNotExist:
        app_user = Spotify_User(name=social.uid)
    app_user.access_token = social.extra_data["access_token"]
    app_user.refresh_token = social.extra_data["refresh_token"]
    app_user.save()
    return render(request, 'spotify/profile.html', {'usuario':app_user})

def log_out(request):
    logout(request)
    # Redirect to a success page.
    return render(request, 'spotify/logout.html', {})
