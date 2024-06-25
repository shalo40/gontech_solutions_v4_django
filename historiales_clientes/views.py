from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import HistorialClienteForm
from .models import HistorialCliente

def crear_historial_cliente(request):
    if request.method == 'POST':
        form = HistorialClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Historial de Cliente creado exitosamente.')
            return redirect('listar_historiales_clientes')
    else:
        form = HistorialClienteForm()
    return render(request, 'historiales_clientes/formulario.html', {'form': form})

def listar_historiales_clientes(request):
    historiales_clientes = HistorialCliente.objects.all()
    return render(request, 'historiales_clientes/listar_historiales_clientes.html', {'historiales_clientes': historiales_clientes})

def editar_historial_cliente(request, id):
    historial_cliente = get_object_or_404(HistorialCliente, id=id)
    if request.method == 'POST':
        form = HistorialClienteForm(request.POST, instance=historial_cliente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Historial de Cliente actualizado exitosamente.')
            return redirect('listar_historiales_clientes')
    else:
        form = HistorialClienteForm(instance=historial_cliente)
    return render(request, 'historiales_clientes/formulario.html', {'form': form})

def eliminar_historial_cliente(request, id):
    historial_cliente = get_object_or_404(HistorialCliente, id=id)
    if request.method == 'POST':
        historial_cliente.delete()
        messages.success(request, 'Historial de Cliente eliminado exitosamente.')
        return redirect('listar_historiales_clientes')
    return render(request, 'historiales_clientes/eliminar_historial_cliente.html', {'historial_cliente': historial_cliente})
