from django.db import models
from django.contrib.auth.models import User

class Vinilo(models.Model):
    artista = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    precio = models.FloatField()

class Reproductor(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    precio = models.FloatField()

class Parlante(models.Model):
    marca = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    potencia = models.CharField(max_length=50)
    precio = models.FloatField()

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='pictures', null=True, blank=True)
    def __str__(self):
        return f'Imagen de: {self.user} - {self.imagen}'