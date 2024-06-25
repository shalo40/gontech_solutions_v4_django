# main/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
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
            messages.success(request, 'Cliente creado exitosamente.')
            return redirect('index')
    else:
        form = ClienteForm()
    return render(request, 'main/formulario.html', {'form': form})

def crear_historial_cliente(request):
    if request.method == 'POST':
        form = HistorialClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Historial de Cliente creado exitosamente.')
            return redirect('index')
    else:
        form = HistorialClienteForm()
    return render(request, 'main/formulario.html', {'form': form})

def crear_solicitud_servicio(request):
    if request.method == 'POST':
        form = SolicitudServicioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Solicitud de Servicio creada exitosamente.')
            return redirect('index')
    else:
        form = SolicitudServicioForm()
    return render(request, 'main/formulario.html', {'form': form})

def crear_tecnico(request):
    if request.method == 'POST':
        form = TecnicoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Técnico creado exitosamente.')
            return redirect('index')
    else:
        form = TecnicoForm()
    return render(request, 'main/formulario.html', {'form': form})

def crear_orden_trabajo(request):
    if request.method == 'POST':
        form = OrdenTrabajoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Orden de Trabajo creada exitosamente.')
            return redirect('index')
    else:
        form = OrdenTrabajoForm()
    return render(request, 'main/formulario.html', {'form': form})

def crear_equipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Equipo creado exitosamente.')
            return redirect('index')
    else:
        form = EquipoForm()
    return render(request, 'main/formulario.html', {'form': form})

def crear_presupuesto(request):
    if request.method == 'POST':
        form = PresupuestoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Presupuesto creado exitosamente.')
            return redirect('index')
    else:
        form = PresupuestoForm()
    return render(request, 'main/formulario.html', {'form': form})

def crear_diagnostico(request):
    if request.method == 'POST':
        form = DiagnosticoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Diagnóstico creado exitosamente.')
            return redirect('index')
    else:
        form = DiagnosticoForm()
    return render(request, 'main/formulario.html', {'form': form})

def crear_pago(request):
    if request.method == 'POST':
        form = PagoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pago registrado exitosamente.')
            return redirect('index')
    else:
        form = PagoForm()
    return render(request, 'main/formulario.html', {'form': form})

def crear_prueba_diagnostico(request):
    if request.method == 'POST':
        form = PruebaDiagnosticoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Prueba de Diagnóstico registrada exitosamente.')
            return redirect('index')
    else:
        form = PruebaDiagnosticoForm()
    return render(request, 'main/formulario.html', {'form': form})

def crear_solicitud_repuesto(request):
    if request.method == 'POST':
        form = SolicitudRepuestoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Solicitud de Repuesto creada exitosamente.')
            return redirect('index')
    else:
        form = SolicitudRepuestoForm()
    return render(request, 'main/formulario.html', {'form': form})

def crear_orden_compra(request):
    if request.method == 'POST':
        form = OrdenCompraForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Orden de Compra creada exitosamente.')
            return redirect('index')
    else:
        form = OrdenCompraForm()
    return render(request, 'main/formulario.html', {'form': form})

def crear_historial_orden_trabajo(request):
    if request.method == 'POST':
        form = HistorialOrdenTrabajoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Historial de Orden de Trabajo creado exitosamente.')
            return redirect('index')
    else:
        form = HistorialOrdenTrabajoForm()
    return render(request, 'main/formulario.html', {'form': form})

def crear_servicio_realizado(request):
    if request.method == 'POST':
        form = ServicioRealizadoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Servicio Realizado registrado exitosamente.')
            return redirect('index')
    else:
        form = ServicioRealizadoForm()
    return render(request, 'main/formulario.html', {'form': form})

def crear_registro_fotografico(request):
    if request.method == 'POST':
        form = RegistroFotograficoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro Fotográfico creado exitosamente.')
            return redirect('index')
    else:
        form = RegistroFotograficoForm()
    return render(request, 'main/formulario.html', {'form': form})
