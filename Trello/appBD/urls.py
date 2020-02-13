from django.urls import path
from . import views

urlpatterns = [
    path('appBD', views.index, name='index'),
    path('create/',views.crearTarjeta, name='crearTarjeta'),
]