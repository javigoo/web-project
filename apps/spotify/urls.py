from django.urls import path, include
from . import views
from django.conf.urls import url
from django.conf import settings

app_name = 'spotify'
urlpatterns = [
    path('', views.home, name='home'),  # Main page where the user can log in or consult the different functionalities of the application
    path('accounts/profile/', views.profile, name='profile'),   # Displays the Spotify profile of the registered user
    path('logout/', views.log_out, name='logout'),
    path('top/', views.top_songs, name='topsongs'),
    path('playlist/', views.playlist_view, name='playlist'),
    path('playlist\\/(?P<playlist_id>[0-9]+)$', views.infoplaylist, name='infoplaylist'),
    path('artist/', views.artist_view, name='artist'),
]
