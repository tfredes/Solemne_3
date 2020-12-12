from django.test import TestCase
from .models import Contacto

# Create your tests here.

class ContactoTestCase(TestCase):
    def setUp(self):
        self.contacto1 = Contacto.objects.create(
            titulo = "Conectividad",
            mensaje = "Fui hacia isla de pascua y tenía super buena señal",
            receptor = "cisnenegro@hispavista.org",
            estado = "recibido")

        self.contacto2 = Contacto.objects.create(
            titulo = "wifi",
            mensaje = "no tengo wifi en casa",
            receptor = "holamundo@desdeplanes.cl",
            estado = "pendiente"
        )
    
    def test_contacto_titulo1 (self):
        self.assertEqual(self.contacto1.titulo, 'Conectividad')
    
    def test_contacto_mensaje1 (self):
        self.assertEqual(self.contacto1.mensaje, 'Apruebo poh')
    
    def test_contacto_receptor1 (self):
        self.assertEqual(self.contacto1.receptor, 'cisnenegro@hispavista.org')

    def test_contacto_estado1 (self):
        self.assertEqual(self.contacto1.estado, 'denegado')

    def test_contacto_titulo2 (self):
        self.assertEqual(self.contacto2.titulo, 'wifi')
    
    def test_contacto_mensaje2 (self):
        self.assertEqual(self.contacto2.mensaje, 'no tengo wifi en casa')
    
    def test_contacto_receptor2 (self):
        self.assertEqual(self.contacto2.receptor, 'holamundo@desdeplanes.cl')

    def test_contacto_estado2 (self):
        self.assertEqual(self.contacto2.estado, 'pendiente')