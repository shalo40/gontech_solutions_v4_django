from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import PresupuestoForm
from .models import Presupuesto

def crear_presupuesto(request):
    if request.method == 'POST':
        form = PresupuestoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Presupuesto creado exitosamente.')
            return redirect('listar_presupuestos')
    else:
        form = PresupuestoForm()
    return render(request, 'presupuestos/formulario.html', {'form': form})

def listar_presupuestos(request):
    presupuestos = Presupuesto.objects.all()
    return render(request, 'presupuestos/listar_presupuestos.html', {'presupuestos': presupuestos})

def editar_presupuesto(request, id):
    presupuesto = get_object_or_404(Presupuesto, id=id)
    if request.method == 'POST':
        form = PresupuestoForm(request.POST, instance=presupuesto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Presupuesto actualizado exitosamente.')
            return redirect('listar_presupuestos')
    else:
        form = PresupuestoForm(instance=presupuesto)
    return render(request, 'presupuestos/formulario.html', {'form': form})

def eliminar_presupuesto(request, id):
    presupuesto = get_object_or_404(Presupuesto, id=id)
    if request.method == 'POST':
        presupuesto.delete()
        messages.success(request, 'Presupuesto eliminado exitosamente.')
        return redirect('listar_presupuestos')
    return render(request, 'presupuestos/eliminar_presupuesto.html', {'presupuesto': presupuesto})
