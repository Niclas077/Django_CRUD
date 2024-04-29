from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def home(request):
    listado_cursos = Curso.objects.all().order_by('creditos')
    
    data = {
        'cursos': listado_cursos
    }
    return render (request,"home.html", data)



def registrar_curso(request):
    nombre = request.POST['txtcurso']
    creditos = request.POST['txtcreditos']
    curso=Curso.objects.create(nombre=nombre,creditos=creditos)
    return redirect('/home')


def eliminar_curso(request, id):
    curso=Curso.objects.get(id=id)
    curso.delete()
    return redirect('/home')

def edicion_curso(request, id):
    curso = Curso.objects.get(id=id)
    data = {
        'titulo': "Edicion de Cursos",
        'curso': curso
    }
    
    return render(request, "edicion.html",data)

def editar_curso(request):
    id = int(request.POST['idcurso'])
    nombre = request.POST['txtcurso']
    creditos = request.POST['txtcreditos']
    
    curso = Curso.objects.get(id=id)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()
    return redirect('/home')
    