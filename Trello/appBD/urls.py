from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crearTar/',views.crearTarjeta, name='crearTarjeta'),
    path('ediTar/',views.editarTarjeta, name='editarTarjeta'),
    path('crearLis/',views.crearLista, name='crearLista'),
    path('ediLis/',views.editarLista, name='editarLista'),
    path('crearTab/',views.crearTablero, name='crearTablero'),
    path('consulTab/',views.consultarTablero, name='consultarTablero'),
    path('ediTab/',views.editarTablero, name='editarTablero'),
]