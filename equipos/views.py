from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import EquipoForm
from .models import Equipo

def crear_equipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Equipo creado exitosamente.')
            return redirect('listar_equipos')
    else:
        form = EquipoForm()
    return render(request, 'equipos/formulario.html', {'form': form})

def listar_equipos(request):
    equipos = Equipo.objects.all()
    return render(request, 'equipos/listar_equipos.html', {'equipos': equipos})

def editar_equipo(request, id):
    equipo = get_object_or_404(Equipo, id=id)
    if request.method == 'POST':
        form = EquipoForm(request.POST, instance=equipo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Equipo actualizado exitosamente.')
            return redirect('listar_equipos')
    else:
        form = EquipoForm(instance=equipo)
    return render(request, 'equipos/formulario.html', {'form': form})

def eliminar_equipo(request, id):
    equipo = get_object_or_404(Equipo, id=id)
    if request.method == 'POST':
        equipo.delete()
        messages.success(request, 'Equipo eliminado exitosamente.')
        return redirect('listar_equipos')
    return render(request, 'equipos/eliminar_equipo.html', {'equipo': equipo})
