
from django.test import TestCase

from .models import *


class PlaylistTestCase(TestCase):

    def setUp(self):
        user = Spotify_User.objects.create(name="user")
        Playlist.objects.create(id=1234567890, name="playlist", duration=10, user=user)

    def test_playlist(self):
        """ Check if the user who created the playlist is correct """
        playlist = Playlist.objects.get(id=1234567890)
        user = Spotify_User.objects.get(name='user')
        self.assertEqual(playlist.user.name, user.name)
