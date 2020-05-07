from django.forms import ModelForm
from apps.spotify.models import Playlist


class PlaylistForm(ModelForm):
    class Meta:
        model = Playlist
        exclude = ('user', 'date',)
