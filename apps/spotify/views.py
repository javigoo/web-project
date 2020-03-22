from django.shortcuts import render
from django.http import HttpResponse, Http404
from apps.spotify.models import *


# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def topSongs(request):
    try:
        lista = Song.objects.order_by('views').reverse()[:10] #Top 10 Songs by views
    except len(lista)==0:
        raise Http404("No tenemos canciones.")
    return render(request, 'topsongs.html', {'topsonglist':lista})
