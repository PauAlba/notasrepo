from django.urls import path
from . import views 

app_name = 'notas'

urlpatterns = [
    path("", views.ListaView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("formulario/", views.FormularioView.as_view(), name="formulario"),
]