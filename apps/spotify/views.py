from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from apps.spotify.models import *
from django.contrib.auth.models import User
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

def profile(request):
    user = request.user #Usuario de django users
    social = user.social_auth.get(provider='spotify') #Usuario de social_django
    token = social.extra_data["access_token"]
    return HttpResponse(token)
    #return render(request, 'spotify/profile.html')
