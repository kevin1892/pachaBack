from rest_framework import serializers
from .models import Artista
class ArtistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artista
        fields=['name']