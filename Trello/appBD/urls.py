from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crearTar/',views.crearTarjeta, name='crearTarjeta'),
    path('consulTar/',views.consultarTarjeta, name='consultarTarjeta'),    
    path('ediTar/',views.editarTarjeta, name='editarTarjeta'),
    path ('elimTarj/<int:id>', views.eliminarTarjeta, name='eliminarTarjeta'),

    path('crearLis/',views.crearLista, name='crearLista'),
    path('consuLis/',views.consultarLista, name='consultarLista'),
    path('ediLis/',views.editarLista, name='editarLista'),
    path ('elimList/<int:id>', views.eliminarLista, name='eliminarLista'),

    path('crearTab/',views.crearTablero, name='crearTablero'),
    path('consulTab/',views.consultarTablero, name='consultarTablero'),
    path('ediTab/',views.editarTablero, name='editarTablero'),      
    path ('elimTab/<int:id>', views.eliminarTablero, name='eliminarTablero'),    
    


    
]