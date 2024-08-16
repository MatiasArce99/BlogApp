from django.db import models

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