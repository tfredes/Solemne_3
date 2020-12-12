from django.db import models

class Contacto (models.Model):
    titulo = models.CharField(max_length=200)
    mensaje = models.TextField()
    receptor = models.CharField(max_length=200)
    estado = models.CharField(max_length=100)
