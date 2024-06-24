# main/views.py

from django.shortcuts import render, redirect
from .forms import (
    ClienteForm, HistorialClienteForm, SolicitudServicioForm, TecnicoForm, OrdenTrabajoForm,
    EquipoForm, PresupuestoForm, DiagnosticoForm, PagoForm, PruebaDiagnosticoForm,
    SolicitudRepuestoForm, OrdenCompraForm, HistorialOrdenTrabajoForm, ServicioRealizadoForm,
    RegistroFotograficoForm
)

def index(request):
    return render(request, 'main/index.html')

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ClienteForm()
    return render(request, 'main/formulario.html', {'form': form})

# Repite este patrón para cada modelo
