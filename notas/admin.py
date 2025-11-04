from django.contrib import admin
from .models import Nota
# Register your models here.

class NotaAdmin(admin.ModelAdmin):
  fields = ["titulo", "contenido"]
  readonly_fields = ["fecha_publicacion"]
  list_display = ["titulo", "contenido", "fecha_publicacion"]
  list_filter = ["fecha_publicacion"]
  search_fields = ["titulo"]


admin.site.register(Nota, NotaAdmin)