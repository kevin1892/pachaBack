from django.db import models
from Canciones.models import Song
from Artistas.models import Artista
# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=150,null=False,default='')
    song_list = models.ManyToManyField(Song)
    artista = models.ForeignKey(Artista,on_delete=models.CASCADE)
    created=models.DateField(auto_now_add=True)