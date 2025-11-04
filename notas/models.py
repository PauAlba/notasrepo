import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Nota(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField("Contenido de la nota...")
    fecha_publicacion = models.DateTimeField("hola", auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete= models.CASCADE, related_name="notas")

    def __str__(self):
        return self.titulo
    