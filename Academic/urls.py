from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('home/', login_required(home), name='home'),
    path('registrarCurso/', registrar_curso),
    path('eliminacionCurso/<int:id>', eliminar_curso),
    path('edicionCurso/<int:id>', edicion_curso),
    path('editarCurso/', editar_curso),
    path('login/', loginView),
    path('logear/', logear),
    path('logoutP/',logoutP),
    path('recuperar/', RecPass),
    path('restaurarP/', resetPassword), 
]

