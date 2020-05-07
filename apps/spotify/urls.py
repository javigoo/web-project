from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'v/users', views.UserViewSet)
router.register(r'v/playlists', views.PlaylistViewSet)

app_name = 'spotify'
urlpatterns = [
    path('', views.home, name='home'),
    # Main page where the user can log in or consult the different functionalities of the application
    path('accounts/profile/', views.profile, name='profile'),  # Displays the Spotify profile of the registered user
    path('logout/', views.log_out, name='logout'),
    path('top/', views.top_songs, name='topsongs'),
    path('playlist/', views.playlist_view, name='playlist'),
    path('playlist\\/(?P<playlist_id>[0-9]+)$', views.infoplaylist, name='infoplaylist'),
    path('artist/', views.artist_view, name='artist'),
    url(r'^', include(router.urls)),

    # Create a playlist, /myrestaurants/restaurants/create/
    path('playlist/create', views.create_playlist, name='create_playlist'),
]
