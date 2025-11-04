from django.urls import path
from . import views 

app_name = 'notas'

urlpatterns = [
  path("", views.lista, name="lista" ),
  #/notas/3
  path("<int:nota_id>/", views.detail, name='detail'),
  path("create/", views.create, name="create"),
  path("formulario/", views.formulario, name='formulario'),
  path("<int:nota_id>/editarForms/", views.editarForms, name='editarForms'),
  path("<int:nota_id>/update/", views.update, name="update"),
  path("<int:nota_id>/delete/", views.delete, name="delete"), 

]