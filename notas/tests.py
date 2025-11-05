from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Nota
import datetime
from django.utils import timezone


# Create your tests here.

def crear_nota(usuario, titulo, dias):
    fecha_publicacion = timezone.now() + datetime.timedelta(days=dias)
    return Nota.objects.create(
        titulo=titulo,
        contenido="Contenido genérico de prueba",
        fecha_publicacion=fecha_publicacion,
        usuario=usuario
    )

class NotModelTest(TestCase):
  def setUp(self):
        #crear un usuario de prueba y autenticarlo para acceder a las vistas
        self.user = User.objects.create_user(username='testuser', password='pass123')
        self.client.login(username='testuser', password='pass123')

  def test_crear_nota(self):
     titulo = 'Nota de prueba'
     contenido = 'Este es el contenido de prueba.'

     nota = Nota.objects.create(
        usuario = self.user,
        titulo = titulo,
        contenido = contenido,
        fecha_publicacion = timezone.now()
     )

     nota.save()

     self.assertEqual(nota.usuario, self.user)
     self.assertEqual(nota.titulo, titulo)
     self.assertEqual(nota.contenido, contenido)
     self.assertIsNotNone(nota.fecha_publicacion)

  def test_retornar_titulo_nota(self):
     titulo = 'Nota de prueba'
     contenido = 'Este es el contenido de prueba.'

     nota = Nota.objects.create(
        usuario = self.user,
        titulo = titulo,
        contenido = contenido,
        fecha_publicacion = timezone.now()
     )

     nota.save()
     self.assertEqual(str(nota), titulo)

class NotaViewsTest(TestCase):
	def setUp(self):
		self.user = User.objects.create_user(username='testuser', password='pass123')
		self.user2 = User.objects.create_user(username='otro', password='pass456')
		self.nota1 = crear_nota(self.user, "Nota propia", 0)
		self.nota2 = crear_nota(self.user2, "Nota ajena", 0)
		self.client.login(username='testuser', password='pass123')

	def test_lista_solo_notas_usuario(self):
		resp = self.client.get(reverse('notas:lista'))
		self.assertEqual(resp.status_code, 200)
		notas = list(resp.context['lista_notas'])
		self.assertIn(self.nota1, notas)
		self.assertNotIn(self.nota2, notas)
		
	def test_lista_requires_login(self):
		self.client.logout()
		resp = self.client.get(reverse('notas:lista'))
		self.assertEqual(resp.status_code, 302)
		self.assertIn('/accounts/login/', resp.url)
		




