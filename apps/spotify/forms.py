from django.forms import ModelForm
from apps.spotify.models import Playlist


class PlaylistForm(ModelForm):
    class Meta:
        model = Playlist
        #fields = '__all__'  # Para registrarlas en spotify, el usuario y el id te lo asignara spoti: ['name', 'duration', 'songs']
        fields = ['name', 'duration', 'songs']