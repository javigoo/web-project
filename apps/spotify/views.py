from django.shortcuts import render
from django.http import HttpResponse
from .models import Song


# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def topSongs(request):
    lista = Song.objects.order_by('-views')[:10] #Top 10 Songs by views
    output = ', '.join([s.name for s in lista])
    return HttpResponse(output)
