from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Song


# Create your views here.
def home(request):
    return render(request, 'spotify/home.html', {})

def topSongs(request):
    try:
        lista = Song.objects.order_by('views')[:10] #Top 10 Songs by views
    except len(lista)==0:
        raise Http404("No tenemos canciones.")
    return render(request, 'spotify/topsongs.html', {'topsonglist':lista})
