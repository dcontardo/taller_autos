from django.shortcuts import render, redirect, get_object_or_404
from .models import Mantencion
from .forms import MantencionForm

def lista_mantenciones(request):
    mantenciones = Mantencion.objects.all()
    return render(request, 'mantenciones/lista.html', {'mantenciones': mantenciones})

def crear_mantencion(request):
    if request.method == 'POST':
        form = MantencionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_mantenciones')
    else:
        form = MantencionForm()
    return render(request, 'mantenciones/crear.html', {'form': form})

def editar_mantencion(request, id):
    mantencion = get_object_or_404(Mantencion, pk=id)
    form = MantencionForm(request.POST or None, instance=mantencion)
    if form.is_valid():
        form.save()
        return redirect('lista_mantenciones')
    return render(request, 'mantenciones/editar.html', {'form': form, 'mantencion': mantencion})

def eliminar_mantencion(request, id):
    mantencion = get_object_or_404(Mantencion, pk=id)
    if request.method == 'POST':
        mantencion.delete()
        return redirect('lista_mantenciones')
    return render(request, 'mantenciones/eliminar.html', {'mantencion': mantencion})
