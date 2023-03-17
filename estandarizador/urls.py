from django.urls import path 
from estandarizador.views import estandarizador,agregar_receta,lista_precios

urlpatterns = [
  path('',estandarizador,name="estandarizador"), 
  path('',lista_precios,name="lista-precios"),
  path('agregar/',agregar_receta,name="agregar-receta"),

]