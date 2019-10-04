from django.db import models


class Distrito(models.Model):
    nombre = models.CharField(max_length=35)

    def __str__(self):
        return self.nombre


class EstadoDenuncia(models.Model):
    nombre = models.CharField(max_length=35)

    def __str__(self):
        return self.nombre


class TipoLugar(models.Model):
    nombre = models.CharField(max_length=35)

    def __str__(self):
        return self.nombre


class TipoDelito(models.Model):
    nombre = models.CharField(max_length=35)

    def __str__(self):
        return self.nombre


class Sexo(models.Model):
    nombre = models.CharField(max_length=12)

    def __str__(self):
        return self.nombre


class ColorPiel(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Contextura(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Municipio(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Localidad(models.Model):
    nombre = models.CharField(max_length=50)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    distrito_no = models.IntegerField()

    def __str__(self):
        return self.nombre



class Denuncia(models.Model):
    fecha_hora = models.DateTimeField()
    identificacion = models.CharField(max_length=30)
    estado = models.ForeignKey(EstadoDenuncia, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=250)
    sintesis = models.TextField()
    agresores_masculinos = models.IntegerField()
    agresores_femeninos = models.IntegerField()
    agresores_desconocidos = models.IntegerField()
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)
    tipo_delito = models.ForeignKey(TipoDelito, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {} ".format(self.identificacion, self.fecha_hora)


class PresuntoAutor(models.Model):
    nombre = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    descripcion = models.TextField()
    contextura = models.ForeignKey(Contextura, on_delete=models.CASCADE)
    sexo = models.ForeignKey(Sexo, on_delete=models.CASCADE)
    color_piel = models.ForeignKey(ColorPiel, on_delete=models.CASCADE)
    estatura_aprox = models.FloatField()
    cabello = models.TextField()
    tatuajes = models.TextField()
    cicatrices = models.TextField()
    denuncia = models.ForeignKey(Denuncia, on_delete=models.CASCADE, related_name='autores')

    def __str__(self):
        return self.nombre



class Victima(models.Model):
    nombre = models.CharField(max_length=60)
    identificacion = models.CharField(max_length=30)
    sexo = models.ForeignKey(Sexo, on_delete=models.CASCADE)
    edad = models.IntegerField()
    denuncia = models.ForeignKey(Denuncia, on_delete=models.CASCADE, related_name='victimas')

    def __str__(self):
        return self.nombre
    


class Testigo(models.Model):
    nombre = models.CharField(max_length=60)
    identificacion = models.CharField(max_length=30)
    sexo = models.ForeignKey(Sexo, on_delete=models.CASCADE)
    edad = models.IntegerField()
    denuncia = models.ForeignKey(Denuncia, on_delete=models.CASCADE, related_name='testigos')

    def __str__(self):
        return self.nombre



class ObjetoUtilizado(models.Model):
    nombre = models.CharField(max_length=70)
    cantidad = models.IntegerField()
    denuncia = models.ForeignKey(Denuncia, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre



class ObjetoAfectado(models.Model):
    nombre = models.CharField(max_length=70)
    cantidad = models.IntegerField()
    denuncia = models.ForeignKey(Denuncia, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
