from django.urls import path
from .views import *

urlpatterns = [
    path('', ventana_inicio, name="inicio"),
    path('vinilosLista/', ViniloListView.as_view(), name='ListarVinilos'),
    path('vinilosDetalle/<pk>', ViniloDetailView.as_view(), name='VinilosDetalle'),
    path('vinilosCrear/', ViniloCreateView.as_view(), name='CrearVinilo'),
    path('vinilosEditar/<pk>', ViniloUpdateView.as_view(), name='EditarVinilo'),
    path('vinilosBorrar/<pk>', ViniloDeleteView.as_view(), name='BorrarVinilo'),
    path('tocadiscosLista/', TocadiscosListView.as_view(), name='ListarTocadiscos'),
    path('tocadiscosDetalle/<pk>', TocadiscosDetailView.as_view(), name='DetalleTocadiscos'),
    path('tocadiscosCrear/', TocadiscosCreateView.as_view(), name='CrearTocadiscos'),
    path('tocadiscosEditar/<pk>', TocadiscosUpdateView.as_view(), name='EditarTocadiscos'),
    path('tocadiscosBorrar/<pk>', TocadiscosDeleteView.as_view(), name='BorrarTocadiscos'),
    path('parlantesLista/', ParlanteListView.as_view(), name='ListarParlantes'),
    path('parlantesDetalle/<pk>', ParlanteDetailView.as_view(), name='DetalleParlantes'),
    path('parlantesCrear/', ParlanteCreateView.as_view(), name='CrearParlantes'),
    path('parlantesEditar/<pk>', ParlanteUpdateView.as_view(), name='EditarParlantes'),
    path('parlantesBorrar/<pk>', ParlanteDeleteView.as_view(), name='BorrarParlantes'),

]