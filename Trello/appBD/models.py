from django.db import models

# Create your models here.

class Tablero(models.Model):                           #creamos la aplicación: python manage.py startapp "miapp"    
    nombreTab = models.CharField(max_length = 30)      #creamos el modelo: python manage.py makemigrations "nuestra app"
                                                        #convertir el modelo a código sql: python manage.py slqmigrate miApp 0001
                                                        #ejecutar el sql: python manage.py migrate
  


class Lista(models.Model):
    nombreList = models.CharField(max_length = 30)
    fkTablero = models.ForeignKey(Tablero, on_delete=models.CASCADE)


class Tarjeta(models.Model):
    nombreTarj = models.CharField(max_length = 30)
    descripcion = models.CharField(max_length = 300)
    fkLista = models.ForeignKey(Lista, on_delete=models.CASCADE)    

