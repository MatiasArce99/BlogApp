from django.urls import path
from .views import *

urlpatterns = [
    path('', ventana_inicio, name="inicio"),
]