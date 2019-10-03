from django.db import models

class ObjetoUtilizado(models.Model):
    nombre = models.CharField(max_length=250)
