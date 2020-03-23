from django.shortcuts import render
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

    client_id = '8ed1089a02664c5a82e1881d283a3031'
    callback_uri = 'http://localhost:8000/'
    scopes = 'user-read-private user-read-email'

    #  La primera llamada es el punto final del servicio '/ authorize',
    #  que le pasa el ID del cliente , los scopes y el URI de redireccionamiento .
    #  Esta es la llamada que inicia el proceso de autenticación para el usuario y
    #  obtiene la autorización del usuario para acceder a los datos.

    oauth = OAuth2Session(client_id, redirect_uri=callback_uri,
                            scope=scopes)

    auth_url, state = oauth.authorization_url('https://accounts.spotify.com/authorize') #Auth_url es la direccion con la que el usuario se identifica.

    return HttpResponse(auth_url)

def after_log(request, auth_url=None, oauth=None): # Una forma de pasarle los argumentos es almacenandolos en la base de datos.

    client_secret = '3ec1a1bb1e3b496684569b51d12bdbda'

    print ('Please go to %s and authorize access.' % auth_url)
    auth_token = input('Enter the full callback URL')

    #  La segunda llamada es al punto final '/ api / token' del Servicio de cuentas
    #  de Spotify, pasándole el código de autorización devuelto por la primera llamada
    #  y la clave secreta del cliente. Esta llamada devuelve un token de acceso y
    #  también un token de actualización.

    access_token = oauth.fetch_token(
        'https://accounts.google.com/o/oauth2/token',
        authorization_response=auth_token,
        client_secret=client_secret)

    access_token = None #El token identifica al usuario en cada sesion. Expira cada hora.
    refresh_token = None #Necesario para actualizar el acces_token.

    return HttpResponse("200Conected")