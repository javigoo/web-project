from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from apps.spotify.models import *
import requests

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, 'spotify/home.html', {})
    else:
        return Http404

def top_songs(request):
    try:
        lista = Song.objects.order_by('views').reverse()[:10] #Top 10 Songs by views
    except len(lista)==0:
        raise Http404("No tenemos canciones.")
    return render(request, 'spotify/topsongs.html', {'topsonglist':lista})