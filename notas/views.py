from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Nota
from django.db.models import F
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class ListaView(LoginRequiredMixin, generic.ListView):
    model = Nota
    template_name = "lista.html"
    context_object_name = "lista_notas"

    def get_queryset(self):
        return Nota.objects.filter(usuario=self.request.user).order_by("-fecha_publicacion")

class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Nota
    template_name = "detalle.html"

    def dispatch(self, request, *args, **kwargs):
        nota = self.get_object()
        if nota.usuario != self.request.user:
            # Aquí hacemos redirect a la lista
            return redirect('notas:lista')
        return super().dispatch(request, *args, **kwargs)

class CrearView(LoginRequiredMixin, CreateView):
    model = Nota
    template_name = "formulario.html"
    fields = ['titulo', 'contenido']
    success_url = reverse_lazy('notas:lista')
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class EditarView(LoginRequiredMixin, UpdateView):
    model = Nota
    template_name = "editar.html"
    fields = ['titulo', 'contenido']
    success_url = reverse_lazy('notas:lista')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.usuario != self.request.user:
            return redirect('notas:lista')
        return super().dispatch(request, *args, **kwargs)

class EliminarView(LoginRequiredMixin, DeleteView):
    model = Nota
    success_url = reverse_lazy('notas:lista')
    template_name = "detalle.html"

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.usuario != self.request.user:
            return redirect('notas:lista')
        return super().dispatch(request, *args, **kwargs)
