from django.shortcuts import render, redirect
from django.forms import ModelForm
from appBD.models import Tarjeta, Lista, Tablero

# Create your views here.

class TarjetaForm(ModelForm):
    class Meta:
        model = Tarjeta
        fields = ['nombreTarj','descripcion','fkLista']

def crearTarjeta(request):
    template = 'appBD/crearTarjeta.html'
    form = TarjetaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('http://127.0.0.1:8000/admin/login/?next=/admin/')
    return render(request, template,{'form':form})
def index(request):
    return render(request, 'appBD/index.html',{})