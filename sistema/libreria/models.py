from django.db import models


# clase libros 
class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='titulo')
    imagen = models.ImageField(upload_to='imagenes/', null=True, verbose_name="imagen")
    descripcion = models.TextField(null=True, verbose_name="descripción")