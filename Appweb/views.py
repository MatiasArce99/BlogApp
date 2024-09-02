from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from .forms import UserRegisterForm, UserEditForm

def ventana_inicio(request):
    return render(request, 'ventanas/inicio.html')

def login_request(request):
    msg_login = ""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            clave = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=clave)
            if user:
                login(request, user)
                print(f'\nInicio de sesión exitosa\n')
                return render(request, 'ventanas/inicio.html')
        msg_login = "Usuario y/o contraseña incorrectos"
    form = AuthenticationForm()
    return render(request, 'ventanas/login.html', {'form': form, 'msg_login': msg_login})

def register(request):
    msg_register = ""
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'ventanas/inicio.html')
        msg_register = "Error al registrar el usuario"
    form = UserRegisterForm()
    return render(request, 'ventanas/register.html', {'form': form, 'msg_register': msg_register})

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        mi_formulario = UserEditForm(request.POST, request.FILES, instance=usuario)
        if mi_formulario.is_valid():
            if mi_formulario.cleaned_data.get('imagen'):
                usuario.avatar.imagen = mi_formulario.cleaned_data.get('imagen')
                usuario.avatar.save()

            mi_formulario.save()
            return render(request, 'ventanas/inicio.html')
    else:
        mi_formulario = UserEditForm(instance=usuario)
    return render(request, 'ventanas/editarPerfil.html', {'form': mi_formulario})

def about(request):
    return render(request, 'ventanas/about.html')

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    return render(request, 'ventanas/inicio.html')

#@login_required()
class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = 'ventanas/cambiar_clave.html'
    success_url = reverse_lazy('EditarPerfil')

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