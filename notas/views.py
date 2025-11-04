from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Nota
from django.urls import reverse
from django.db.models import F
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.contrib.auth.decorators import login_required



# Create your tests here.
def lista(request):

    lista_notas = Nota.objects.order_by("fecha_publicacion")
    contexto = {"lista_notas": lista_notas}
    return render(request, "lista.html", contexto)

class ListaView(LoginRequiredMixin, generic.ListView):
    model = Nota
    template_object_name = "lista_notas"

    #con esto de abajo ya no debe de permitir al usuario editar o eliminar notas de otros segun
    def get_queryset(self):
        print(self.request.user)
        return Nota.objects.order_by("-fecha_publicacion")

# Ver el detalle de una pregunta
def detail(request, nota_id):
  nota = get_object_or_404(Nota, pk=nota_id)
  return render(request, "detalle.html", {"nota":nota})

class DetailView(LoginRequiredMixin, generic.DetailView):
    model: Nota 
    template_name = "detalle.html"

def formulario(request):
    return render(request, 'formulario.html')

class FormularioView(LoginRequiredMixin, generic.FormView):
    model = Nota 
    template_name = "formulario.html"

def editarForms(request, nota_id):
    nota = get_object_or_404(Nota, pk=nota_id)
    return render(request,'editar.html', {"nota": nota})

class FormularioView(LoginRequiredMixin, generic.FormView):
    model = Nota 
    template_name = "editar.html"

@login_required
def create(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo")
        contenido = request.POST.get("contenido")

        Nota.objects.create(titulo=titulo, contenido=contenido)
        return redirect("notas:lista")  
    return render(request, "formulario.html")

@login_required
def delete(request, nota_id):
    nota = get_object_or_404(Nota, pk=nota_id)
    if request.method == "POST":
        nota.delete()
        return redirect("notas:lista")
    return HttpResponseRedirect(reverse("notas:lista"))

@login_required
def update(request, nota_id):
    nota = get_object_or_404(Nota, pk=nota_id)

    if request.method == "POST":
        titulo = request.POST.get("titulo", "").strip()
        contenido = request.POST.get("contenido", "").strip()

        if not titulo:
            return render(request, "notas/update.html", {
                "nota": nota,
                "error": "El título es obligatorio.",
                "titulo": titulo,
                "contenido": contenido,
            })

        nota.titulo = titulo
        nota.contenido = contenido
        nota.save()

        return HttpResponseRedirect(reverse("notas:lista"))
