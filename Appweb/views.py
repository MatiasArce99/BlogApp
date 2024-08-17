from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *

def ventana_inicio(request):
    return render(request, 'ventanas/inicio.html')

class ViniloListView(ListView):
    model = Vinilo
    context_object_name = 'vinilo'
    template_name = 'ventanas/vinilos_lista.html'

class ViniloDetailView(DetailView):
    model = Vinilo
    template_name = 'ventanas/vinilos_detalle.html'

class ViniloCreateView(CreateView):
    model = Vinilo
    template_name = 'ventanas/vinilos_crear.html'
    success_url = reverse_lazy('ListarVinilos')
    fields = ['artista', 'album', 'genero', 'precio']

class ViniloUpdateView(UpdateView):
    model = Vinilo
    template_name = 'ventanas/vinilos_editar.html'
    success_url = reverse_lazy('ListarVinilos')
    fields = ['artista', 'album', 'genero', 'precio']

class ViniloDeleteView(DeleteView):
    model = Vinilo
    template_name = 'ventanas/vinilos_borrar.html'
    success_url = reverse_lazy('ListarVinilos')

class TocadiscosListView(ListView):
    model = Reproductor
    context_object_name = 'reproductor'
    template_name = 'ventanas/tocadiscos_lista.html'

class TocadiscosDetailView(DetailView):
    model = Reproductor
    template_name = 'ventanas/tocadiscos_detalle.html'

class TocadiscosCreateView(CreateView):
    model = Reproductor
    template_name = 'ventanas/tocadiscos_crear.html'
    success_url = reverse_lazy('ListarTocadiscos')
    fields = ['marca', 'modelo', 'precio']

class TocadiscosUpdateView(UpdateView):
    model = Reproductor
    template_name = 'ventanas/tocadiscos_editar.html'
    success_url = reverse_lazy('ListarTocadiscos')
    fields = ['marca', 'modelo', 'precio']

class TocadiscosDeleteView(DeleteView):
    model = Reproductor
    template_name = 'ventanas/tocadiscos_borrar.html'
    success_url = reverse_lazy('ListarTocadiscos')

class ParlanteListView(ListView):
    model = Parlante
    context_object_name = 'parlante'
    template_name = 'ventanas/parlantes_lista.html'

class ParlanteDetailView(DetailView):
    model = Parlante
    template_name = ''

class ParlanteCreateView(CreateView):
    model = Parlante
    template_name = ''
    success_url = reverse_lazy('ListarParlantes')
    fields = ['marca', 'tipo', 'potencia', 'precio']

class ParlanteUpdateView(UpdateView):
    model = Parlante
    template_name = ''
    success_url = reverse_lazy('ListarParlantes')
    fields = ['marca', 'tipo', 'potencia', 'precio']

class ParlanteDeleteView(DeleteView):
    model = Parlante
    template_name = ''
    success_url = reverse_lazy('ListarParlantes')