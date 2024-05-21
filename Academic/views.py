from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.http import HttpResponse
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
    return redirect(request,'/home')

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
    
    
def loginView(request):
    return render(request,'login.html')


def logear (request):
    if request.method == 'POST':
        username = request.POST['txtemail']
        password = request.POST['txtpassword']
        user = authenticate(request, username=username, password=password)
        if (user is not None):
            login(request, user)
            return redirect('/home')
        else:
            print("No se ha podido logear")
            return render(request, 'login.html', {'error message': 'Credenciales invalidas'})
    else:
        return render(request, 'login.html')
        
def RecPass(request):
    return render(request,'rectpass.html')
    
def logoutP(request):
    logout(request)
    return redirect('/login')


def resetPassword(request):
    if request.method == 'POST':
        txtusuario = request.POST['txtusuario'] 
        txtpassword = request.POST['txtcontraseña']
        try:
            
            user = User.objects.get(email=txtusuario)
            user.set_password(txtpassword)
            user.save()
            #messages.success("Actualizacion realizada con exito")
            return redirect('/login')
        except User.DoesNotExist:
            #messages.error(request, "No existe una cuenta asociada con esta direccion de correo, intentelo nuevamente")
            return redirect('/recuperar')
    else:
        return HttpResponse("Metodo no permitido", status=405)

