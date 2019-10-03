from django.db import models

class TipoLugar(models.Model):
    nombre = models.CharField(max_length=35)


class TipoDelito(models.Model):
    nombre = models.CharField(max_length=35)


#class Sexo(models.Model):
#    nombre = models.CharField(max_length=1)


#class Municipio(models.Model):
#    nombre = models.CharField(max_length=100)


class Localidad(models.Model):
    nombre = models.CharField(max_length=50)
    municipio = models.CharField(max_length=30)
    distrito_no = models.IntegerField()


class PresuntoAutor(models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.TextField(max)
    color_piel = models.CharField(max_length=15)
    estatura_aprox = models.FloatField()
    cabello = models.TextField(max)
    contextura = models.CharField(max_length=15)
    tatuajes = models.TextField(max)
    cicatrices = models.TextField(max)
    sexo = models.CharField(max_length=12)
    alias = models.CharField(max_length=60)


class ObjetoUtilizado(models.Model):
    nombre = models.CharField(max_length=70)
    cantidad = models.IntegerField()


class ObjetoAfectado(models.Model):
    nombre = models.CharField(max_length=70)
    cantidad = models.IntegerField()