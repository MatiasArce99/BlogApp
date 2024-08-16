from django.shortcuts import render
from django.views.generic import ListView
from .models import *

def ventana_inicio(request):
    return render(request, 'ventanas/inicio.html')

class ViniloListView(ListView):
    model = Vinilo
    context_object_name = 'vinilo'
    template_name = 'ventanas/vinilos_lista.html'