from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Song
from .serializers import SongSerializer
# Create your views here.
class SongViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Song.objects.all()
    serializer_class = SongSerializer