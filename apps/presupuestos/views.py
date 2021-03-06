from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .models import Presupuesto, Categoria
from .forms import PresupuestoForm, CategoriaForm

@login_required
def crear_presupuesto(request):
    if request.method == 'POST':
        form = PresupuestoForm(request.POST)
        if form.is_valid():
            presupuesto = form.save(commit=False)
            presupuesto.nombre = form.cleaned_data["nombre"]
            presupuesto.total_planeado = 0
            presupuesto.total_actual = 0
            presupuesto.usuario = request.user
            presupuesto.save()
            messages.success(request, 'El presupuesto se registró correctamente.')
            return redirect('presupuestos:registrar_categoria', id_presupuesto=presupuesto.id)
        else:
            messages.error(request, 'No se pudo registrar el presupuesto, por favor verifique los datos ingresados.')
    else:
        form = PresupuestoForm()
    return render(request, 'presupuestos/presupuestos_form.html', {
        'form': form
    })


@login_required
def mis_presupuestos(request):
    presupuestos = request.user.presupuestos_del_usuario.filter(estado="Activo")
    return render(request, 'presupuestos/listado_de_presupuestos.html',{'presupuestos':presupuestos})


class EditarPresupuesto(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Presupuesto
    form_class = PresupuestoForm
    template_name = 'presupuestos/presupuesto_editar.html'
    success_message = "El presupuesto %(nombre) s se modificó correctamente."
    success_url = reverse_lazy('presupuestos:listado_de_presupuestos')

@login_required
def desactivar_presupuesto(request, id_presupuesto):
    presupuesto = get_object_or_404(Presupuesto, pk=id_presupuesto)
    presupuesto.estado = "Inactivo"
    presupuesto.save()
    return redirect('presupuestos:listado_de_presupuestos')

@login_required
def crear_categoria(request, id_presupuesto):
    presupuesto = get_object_or_404(Presupuesto, pk=id_presupuesto)
    form_class = CategoriaForm
    if request.method == "POST":
        form = form_class(request.POST)
        if form.is_valid():
            categoria = form.save(commit=False)
            categoria.presupuesto = presupuesto
            categoria.nombre = form.cleaned_data["nombre"]
            categoria.planeado = form.cleaned_data["planeado"]
            categoria.actual = 0
            categoria.diferencia = form.cleaned_data["planeado"]
            presupuesto.total_planeado += categoria.planeado
            categoria.save()
            presupuesto.save()
            messages.success(request, 'La categoria se registró correctamente.')
            return redirect('presupuestos:listado_de_categorias', id_presupuesto)
        else:
            messages.error(request, "Error")
    return render(request, 'presupuestos/categorias_form.html', {'form':form_class(), 'id_presupuesto':id_presupuesto})


@login_required
def listado_de_categorias_del_presupuesto(request, id_presupuesto):
    presupuesto = get_object_or_404(Presupuesto, pk=id_presupuesto)
    categorias = presupuesto.categorias_del_presupuesto.all()
    nombre_presupuesto = presupuesto.nombre
    return render(request, 'presupuestos/listado_de_categorias.html',{'categorias':categorias, 
        'nombre_presupuesto': nombre_presupuesto, 'id_presupuesto':id_presupuesto})

@login_required
def EditarCategoriaF(request,pk):
    categoria = Categoria.objects.get(id=pk)
    if request.method == 'GET':
        form = CategoriaForm(instance=categoria)
    else:
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            categoria = form.save(commit=False)
            actualizarCategoria(categoria.id, categoria.planeado)
            #categoria.save()
        return redirect('presupuestos:listado_de_categorias', categoria.presupuesto.id)
    return render(request, 'presupuestos/categoria_editar.html', {'form':form, 'id_presupuesto':categoria.presupuesto.id})

def actualizarCategoria(idCategoria, inPlaneado):
    categoriaOld = Categoria.objects.get(id=idCategoria)
    presupuesto = Presupuesto.objects.get(id=str(categoriaOld.presupuesto.id))
    presupuesto.total_planeado -=  categoriaOld.planeado
    presupuesto.total_planeado += inPlaneado
    if categoriaOld.actual != 0:
        categoriaOld.diferencia = (inPlaneado - categoriaOld.actual)
    else:
        print("ENTRO POR AQUI")
        categoriaOld.diferencia = inPlaneado
    categoriaOld.planeado = inPlaneado
    presupuesto.save()
    categoriaOld.save()
