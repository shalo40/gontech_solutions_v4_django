from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import TecnicoForm # type: ignore
from .models import Tecnico

def crear_tecnico(request):
    if request.method == 'POST':
        form = TecnicoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Técnico creado exitosamente.')
            return redirect('listar_tecnicos')
    else:
        form = TecnicoForm()
    return render(request, 'tecnicos/formulario.html', {'form': form})

def listar_tecnicos(request):
    tecnicos = Tecnico.objects.all()
    return render(request, 'tecnicos/listar_tecnicos.html', {'tecnicos': tecnicos})

def editar_tecnico(request, id):
    tecnico = get_object_or_404(Tecnico, id=id)
    if request.method == 'POST':
        form = TecnicoForm(request.POST, instance=tecnico)
        if form.is_valid():
            form.save()
            messages.success(request, 'Técnico actualizado exitosamente.')
            return redirect('listar_tecnicos')
    else:
        form = TecnicoForm(instance=tecnico)
    return render(request, 'tecnicos/formulario.html', {'form': form})

def eliminar_tecnico(request, id):
    tecnico = get_object_or_404(Tecnico, id=id)
    if request.method == 'POST':
        tecnico.delete()
        messages.success(request, 'Técnico eliminado exitosamente.')
        return redirect('listar_tecnicos')
    return render(request, 'tecnicos/eliminar_tecnico.html', {'tecnico': tecnico})
