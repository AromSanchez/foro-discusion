from django.shortcuts import render, get_object_or_404, redirect
from .models import Tema, Respuesta

# Create your views here.
def lista_temas(request):
    temas = Tema.objects.all().order_by('-fecha')
    return render(request, 'foros/lista_temas.html', {'temas': temas})


def detalle_tema(request, pk):
    tema = get_object_or_404(Tema, pk=pk)
    return render(request, 'foros/detalle_tema.html', {'tema': tema})


def crear_tema(request):
    error = None
    if request.method == 'POST':
        titulo = request.POST.get('titulo', '').strip()
        autor = request.POST.get('autor', '').strip()
        imagen = request.FILES.get('imagen')
        if not titulo or not autor:
            error = 'Título y autor son requeridos.'
        else:
            tema = Tema.objects.create(titulo=titulo, autor=autor, imagen=imagen)
            return redirect('detalle_tema', pk=tema.pk)
    return render(request, 'foros/tema_form.html', {'error': error})


def editar_tema(request, pk):
    tema = get_object_or_404(Tema, pk=pk)
    error = None
    if request.method == 'POST':
        titulo = request.POST.get('titulo', tema.titulo).strip()
        autor = request.POST.get('autor', tema.autor).strip()
        imagen = request.FILES.get('imagen')
        if not titulo or not autor:
            error = 'Título y autor son requeridos.'
        else:
            tema.titulo = titulo
            tema.autor = autor
            if imagen:
                tema.imagen = imagen
            tema.save()
            return redirect('detalle_tema', pk=tema.pk)
    return render(request, 'foros/tema_form.html', {'tema': tema, 'error': error})


def eliminar_tema(request, pk):
    tema = get_object_or_404(Tema, pk=pk)
    if request.method == 'POST':
        tema.delete()
        return redirect('lista_temas')
    return render(request, 'foros/tema_confirm_delete.html', {'object': tema})


def crear_respuesta(request, tema_id):
    tema = get_object_or_404(Tema, pk=tema_id)
    error = None
    if request.method == 'POST':
        texto = request.POST.get('texto', '').strip()
        autor = request.POST.get('autor', '').strip()
        if not texto or not autor:
            error = 'Texto y autor son requeridos.'
        else:
            Respuesta.objects.create(tema=tema, texto=texto, autor=autor)
            return redirect('detalle_tema', pk=tema.pk)
    return render(request, 'foros/respuesta_form.html', {'tema': tema, 'error': error})


def editar_respuesta(request, pk):
    respuesta = get_object_or_404(Respuesta, pk=pk)
    error = None
    if request.method == 'POST':
        texto = request.POST.get('texto', respuesta.texto).strip()
        autor = request.POST.get('autor', respuesta.autor).strip()
        if not texto or not autor:
            error = 'Texto y autor son requeridos.'
        else:
            respuesta.texto = texto
            respuesta.autor = autor
            respuesta.save()
            return redirect('detalle_tema', pk=respuesta.tema.pk)
    return render(request, 'foros/respuesta_form.html', {'tema': respuesta.tema, 'respuesta': respuesta, 'error': error})


def eliminar_respuesta(request, pk):
    respuesta = get_object_or_404(Respuesta, pk=pk)
    if request.method == 'POST':
        tema_pk = respuesta.tema.pk
        respuesta.delete()
        return redirect('detalle_tema', pk=tema_pk)
    return render(request, 'foros/respuesta_confirm_delete.html', {'object': respuesta})
