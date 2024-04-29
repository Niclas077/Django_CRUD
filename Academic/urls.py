from django.urls import path
from .views import *

urlpatterns = [
    
    path('home/', home),
    path('registrarCurso/', registrar_curso),
    path('eliminacionCurso/<int:id>', eliminar_curso),
    path('edicionCurso/<int:id>', edicion_curso),
    path('editarCurso/', editar_curso)
    
]
