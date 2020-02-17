from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from appBD.models import Tarjeta, Lista, Tablero

# Create your views here.

class TarjetaForm(ModelForm):
    class Meta:
        model = Tarjeta
        fields = ['nombreTarj','descripcion','fkLista']

class ListaForm(ModelForm):
    class Meta:
        model = Lista
        fields = ['nombreList','fkTablero']

class TableroForm(ModelForm):
    class Meta:
        model = Tablero
        fields = ['nombreTab']

def index(request):
    return render(request, 'appBD/index.html',{})

def crearTarjeta(request):
    template = 'appBD/crearTarjeta.html'
    form = TarjetaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('consultarTarjeta')
    return render(request, template,{'form':form})

def crearLista(request):
    template = 'appBD/crearLista.html'
    form = ListaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('consultarLista')
    return render(request, template,{'form':form})

def crearTablero(request):
    template = 'appBD/crearTablero.html'
    form = TableroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('consultarTablero')
    return render(request, template,{'form':form})

def consultarTarjeta(request):
    template = 'appBD/consultarTarjeta.html'
    listadotarjeta = Tarjeta.objects.all()
    contexto = {}
    contexto['object_list'] = listadotarjeta
    return render (request, template, contexto)

def consultarLista(request):
    template = 'appBD/consultarLista.html'
    listadolista = Lista.objects.all()
    contexto = {}
    contexto['object_list'] = listadolista
    return render (request, template, contexto)

def consultarTablero(request):
    template = 'appBD/consultarTablero.html'
    listadotablero = Tablero.objects.all()
    contexto = {}
    contexto['object_list'] = listadotablero
    return render (request, template, contexto)

def editarTarjeta(request, id):
    template = 'appBD/editarTarjeta.html'
    info_tarjeta = get_object_or_404(Tarjeta,pk=id)
    form = TarjetaForm(request.POST or None, instance= info_tarjeta )
    if form.is_valid():
        form.save()
        return redirect('consultarTarjeta')
    return render(request,template,{'form':form})

def editarLista(request, id):
    template = 'appBD/editarLista.html'
    info_lista = get_object_or_404(Lista,pk=id)
    form = ListaForm(request.POST or None, instance= info_lista )
    if form.is_valid():
        form.save()
        return redirect('consultarLista')
    return render(request,template,{'form':form})

def editarTablero(request, id):
    template = 'appBD/editarTablero.html'
    info_tablero = get_object_or_404(Tablero,pk=id)
    form = TableroForm(request.POST or None, instance= info_tablero )
    if form.is_valid():
        form.save()
        return redirect('consultarTablero')
    return render(request,template,{'form':form})