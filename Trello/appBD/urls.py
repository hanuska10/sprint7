from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crearTar/',views.crearTarjeta, name='crearTarjeta'),
    path('ediTar/<int:id>',views.editarTarjeta, name='editarTarjeta'),
    path ('elimTarj/<int:id>', views.eliminarTarjeta, name='eliminarTarjeta'),

    path('crearLis/',views.crearLista, name='crearLista'),
    path('ediLis/<int:id>',views.editarLista, name='editarLista'),
    path ('elimList/<int:id>', views.eliminarLista, name='eliminarLista'),

    path('crearTab/',views.crearTablero, name='crearTablero'),    
    path('ediTab/<int:id>',views.editarTablero, name='editarTablero'),      
    path ('elimTab/<int:id>', views.eliminarTablero, name='eliminarTablero'),    
    
    path('consulTab/',views.consultarTablero, name='consultarTablero'),
   

    
]