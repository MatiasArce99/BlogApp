from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from .forms import UserRegisterForm

def ventana_inicio(request):
    return render(request, 'ventanas/inicio.html')

@login_required
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            clave = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
                return render(request, 'ventanas/inicio.html', {'mensaje':f'Bienvenido {usuario}'})
            else:
                return render(request, 'ventanas/inicio.html', {'mensaje':'Error. Datos incorrectos'})
        else:
            return render(request, 'ventanas/inicio.html', {'mensaje':'Error. Formulario invalido'})
    form = AuthenticationForm()
    return render(request, 'ventanas/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'ventanas/inicio.html', {'mensaje':'Usuario creado'})
    else:
        form = UserRegisterForm(request.POST)
    return render(request, 'ventanas/register.html', {'form':form})

@login_required
def editarPerfil(request):
    usuario = request.user
    #if request.method == 'POST':

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