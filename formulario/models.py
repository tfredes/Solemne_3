from django.db import models

# Create your models here.


class Formulario(models.Model):
    nombre = models.TextField(max_length=40)
    apellido = models.TextField(max_length=40)
    rut = models.TextField(max_length=20)
    telefono = models.TextField(default=None, max_length=20)
    nserie = models.TextField(max_length=15)
    email = models.TextField(max_length=30)

