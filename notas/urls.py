from django.urls import path
from . import views 

app_name = 'notas'

urlpatterns = [
    path("", views.ListaView.as_view(), name="lista"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("crear/", views.CrearView.as_view(), name="crear"),
    path("<int:pk>/editar/", views.EditarView.as_view(), name="editar"),
    path("<int:pk>/eliminar/", views.EliminarView.as_view(), name="eliminar"),
]