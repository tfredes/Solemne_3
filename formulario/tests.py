from django.test import TestCase
from .models import Formulario

# Create your tests here.

class FormularioTestCase(TestCase):
    def setUp(self):
        self.formulario1 = Formulario.objects.create(
            nombre="Jonathan",
            apellido="Yon",
            rut="17.551.893-3",
            telefono=84899358,
            nserie="511.456.992",
            email="jonathan.yon@gmail.com")
        self.formulario2 = Formulario.objects.create(
            nombre="Bryan",
            apellido="Avendano",
            rut="17.924.761-k",
            telefono=93458912,
            nserie="503.679.435",
            email="bryan.avendano@altavista.com")

    def test_formulario_nombre(self):
        self.assertEqual(self.formulario1.nombre, 'Jonathan')

    def test_formulario_nombre2(self):
        self.assertEqual(self.formulario2.nombre, 'Bryan')
    
    def test_formulario_apellido1(self):
        self.assertEqual(self.formulario1.apellido, 'Yon')
    
    def test_formulario_apellido2(self):
        self.assertEqual(self.formulario2.apellido, 'Avendano')

    def test_formulario_rut(self):
        self.assertEqual(self.formulario1.rut, '17.551.893-3')

    def test_formulario_rut2(self):
        self.assertEqual(self.formulario2.rut, '17.924.761-k')    

    def test_formulario_telefono1(self):
        self.assertEqual(self.formulario1.telefono, 84899358)    

    def test_formulario_telefono2(self):
        self.assertEqual(self.formulario2.telefono, 93458912)

    def test_formulario_nserie1(self):
        self.assertEqual(self.formulario1.nserie, '511.456.992')  

    def test_formulario_nserie2(self):
        self.assertEqual(self.formulario2.nserie, '503.679.435') 

    def test_formulario_email1(self):
        self.assertEqual(self.formulario1.email, 'jonathan.yon@gmail.com')    

    def test_formulario_email2(self):
        self.assertEqual(self.formulario2.email, 'bryan.avendano@altavista.com')