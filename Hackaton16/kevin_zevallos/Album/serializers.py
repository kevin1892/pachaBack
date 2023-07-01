from rest_framework import serializers
from .models import Album
from Canciones.serializers import SongSerializer
class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields=['song_list']