from django.conf.urls import url
from django.urls import path, include

from . import views

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

    path('playlist/create', views.create_playlist, name='create_playlist'),     # Create a playlist
    path('playlist/update/<str:pk>/', views.update_playlist, name='update_playlist'),
    path('playlist/delete/<str:pk>/', views.delete_playlist, name='delete_playlist'),

]
