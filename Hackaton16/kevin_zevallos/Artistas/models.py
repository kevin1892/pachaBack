from django.db import models

# Create your models here.
class Artista(models.Model):
    name = models.CharField(max_length=50,null=False,default='')