from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
    apellido = forms.CharField(label='Apellido', widget=forms.TextInput)
    nombre = forms.CharField(label='Nombre', widget=forms.TextInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'apellido', 'nombre']
        help_texts = {k: '' for k in fields}

class UserEditForm(UserChangeForm):
    password = None
    email = forms.EmailField(label='Ingrese su correo: ')
    apellido = forms.CharField(label='Apellido: ', required=False)
    nombre = forms.CharField(label='Nombre: ', required=False)
    imagen = forms.ImageField(label='Imagen: ', required=False)

    class Meta:
        model = User
        fields = ['email', 'apellido', 'nombre']