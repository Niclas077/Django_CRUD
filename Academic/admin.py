from django.contrib import admin
from .models import *


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
 list_display = ('id','nombre','creditos')   
 list_display_links = ('nombre',)
 
def datos(self, obj):
    return obj.nombre.upper()

    
@admin.register(Docente)
class docenteAdmin(admin.ModelAdmin):
    list_display =('id','apellido_paterno','apellido_materno', 'nombres', 'fecha_nacimiento', 'sexo')


