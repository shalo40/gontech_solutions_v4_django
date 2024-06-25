from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import SolicitudServicioForm
from .models import SolicitudServicio

def crear_solicitud_servicio(request):
    if request.method == 'POST':
        form = SolicitudServicioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Solicitud de Servicio creada exitosamente.')
            return redirect('listar_solicitudes_servicio')
    else:
        form = SolicitudServicioForm()
    return render(request, 'solicitudes_servicio/formulario.html', {'form': form})

def listar_solicitudes_servicio(request):
    solicitudes_servicio = SolicitudServicio.objects.all()
    return render(request, 'solicitudes_servicio/listar_solicitudes_servicio.html', {'solicitudes_servicio': solicitudes_servicio})

def editar_solicitud_servicio(request, id):
    solicitud_servicio = get_object_or_404(SolicitudServicio, id=id)
    if request.method == 'POST':
        form = SolicitudServicioForm(request.POST, instance=solicitud_servicio)
        if form.is_valid():
            form.save()
            messages.success(request, 'Solicitud de Servicio actualizada exitosamente.')
            return redirect('listar_solicitudes_servicio')
    else:
        form = SolicitudServicioForm(instance=solicitud_servicio)
    return render(request, 'solicitudes_servicio/formulario.html', {'form': form})

def eliminar_solicitud_servicio(request, id):
    solicitud_servicio = get_object_or_404(SolicitudServicio, id=id)
    if request.method == 'POST':
        solicitud_servicio.delete()
        messages.success(request, 'Solicitud de Servicio eliminada exitosamente.')
        return redirect('listar_solicitudes_servicio')
    return render(request, 'solicitudes_servicio/eliminar_solicitud_servicio.html', {'solicitud_servicio': solicitud_servicio})
