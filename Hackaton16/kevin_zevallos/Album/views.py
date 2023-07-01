from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Album
from .serializers import AlbumSerializer
# Create your views here.
class AlbumViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer