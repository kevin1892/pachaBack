from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Artista
from .serializers import ArtistaSerializer
# Create your views here.
class ArtistaViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Artista.objects.all()
    serializer_class = ArtistaSerializer
