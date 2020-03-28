from django.test import TestCase
from apps.spotify.models import *

# Create your tests here.

class PlaylistTest(TestCase):
    pass

    """
    def setUp(self):
        User.objects.create(name='carlos')
        Playlist.objects.create(id='1234', name='pop', duration=124, user=User.objects.get(name='carlos'))

    def test_playlist_creation(self):
        pop = Playlist.objects.get(name='pop')
        carlos = User.objects.get(name='carlos')
        print(pop.user.name)
        print(carlos.name)
        self.assertEqual( pop.user.name, carlos.name)
    """

# Test travis (commit)
