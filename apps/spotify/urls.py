from django.urls import path, include
from . import views
from django.conf.urls import url
from django.conf import settings

app_name = 'spotify'
urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/profile/', views.profile, name='profile'),   # Muestra el perfil de Spotify del usuario registrado
    path('logout/', views.log_out, name='logout'),
    path('top/', views.top_songs, name='topsongs'),
    path('playlist/', views.playlist_view, name='playlist'),
    path('playlist\\/(?P<playlist_id>[0-9]+)$', views.infplaylist, name='infoplaylist'),
]
