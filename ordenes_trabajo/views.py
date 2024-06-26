from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import OrdenTrabajoForm
from .models import OrdenTrabajo

def crear_orden_trabajo(request):
    if request.method == 'POST':
        form = OrdenTrabajoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Orden de trabajo creada exitosamente.')
            return redirect('listar_ordenes_trabajo')
    else:
        form = OrdenTrabajoForm()
    return render(request, 'ordenes_trabajo/formulario.html', {'form': form})

def listar_ordenes_trabajo(request):
    ordenes_trabajo = OrdenTrabajo.objects.all()
    return render(request, 'ordenes_trabajo/listar_ordenes_trabajo.html', {'ordenes_trabajo': ordenes_trabajo})

def editar_orden_trabajo(request, id):
    orden_trabajo = get_object_or_404(OrdenTrabajo, id=id)
    if request.method == 'POST':
        form = OrdenTrabajoForm(request.POST, instance=orden_trabajo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Orden de trabajo actualizada exitosamente.')
            return redirect('listar_ordenes_trabajo')
    else:
        form = OrdenTrabajoForm(instance=orden_trabajo)
    return render(request, 'ordenes_trabajo/formulario.html', {'form': form})

def eliminar_orden_trabajo(request, id):
    orden_trabajo = get_object_or_404(OrdenTrabajo, id=id)
    if request.method == 'POST':
        orden_trabajo.delete()
        messages.success(request, 'Orden de trabajo eliminada exitosamente.')
        return redirect('listar_ordenes_trabajo')
    return render(request, 'ordenes_trabajo/eliminar_orden_trabajo.html', {'orden_trabajo': orden_trabajo})
