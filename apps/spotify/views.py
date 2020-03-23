from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from apps.spotify.models import *
import requests
from requests_oauthlib import OAuth2Session

# Create your views here.
def home(request):
    return render(request, 'spotify/home.html', {})

def top_songs(request):
    try:
        lista = Song.objects.order_by('views').reverse()[:10] #Top 10 Songs by views
    except len(lista)==0:
        raise Http404("No tenemos canciones.")
    return render(request, 'spotify/topsongs.html', {'topsonglist':lista})



def before_log(request):

    #  La primera llamada es el punto final del servicio '/ authorize',
    #  que le pasa el ID del cliente , los scopes y el URI de redireccionamiento .
    #  Esta es la llamada que inicia el proceso de autenticación para el usuario y
    #  obtiene la autorización del usuario para acceder a los datos.

    user = User()
    client_id = '8ed1089a02664c5a82e1881d283a3031'
    callback_uri = 'http://localhost:8000/after_log_'+str(user.id)   #SPOTIFY NO NOS PERMITE QUE CADA UNA SEA DISTINTA.
    oauth = OAuth2Session(client_id, redirect_uri= 'https://www.google.com/',
                            scope='user-read-private user-read-email')

    auth_url, state = oauth.authorization_url('https://accounts.spotify.com/authorize') #Auth_url es la direccion con la que el usuario se identifica.

    setattr(user, 'auth_url', auth_url)
    user.save()

    return HttpResponse(auth_url) # Tmb se puede poner directamente la variable.

def after_log(request, id):
     # Una forma de pasarle los argumentos es almacenandolos en la base de datos.
    user = get_object_or_404(User, id=id)
    
    client_secret = '3ec1a1bb1e3b496684569b51d12bdbda'
    client_id = '8ed1089a02664c5a82e1881d283a3031'
    callback_uri = 'http://localhost:8000/after_log_'+str(user.id)

    print ('Please go to %s and authorize access.' % user.auth_url)
    auth_token = input('Enter the full callback URL')

    #  La segunda llamada es al punto final '/ api / token' del Servicio de cuentas
    #  de Spotify, pasándole el código de autorización devuelto por la primera llamada
    #  y la clave secreta del cliente. Esta llamada devuelve un token de acceso y
    #  también un token de actualización.

    oauth = OAuth2Session(client_id, redirect_uri= callback_uri,
                            scope='user-read-private user-read-email')

    access_token = oauth.fetch_token(
        'https://accounts.spotify.com/api/token',
        authorization_response=auth_token,
        client_secret=client_secret)

    #setattr(user, 'access_token', access_token)
    #user.save()
    #setattr(user, 'refresh_token', refresh_token)
    #user.save()

    return HttpResponse(access_token)