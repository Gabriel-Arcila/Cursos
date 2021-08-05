from django.contrib import admin
from gestionCursos.models import Curso, Notificacion, Categoria, CursosUsuarios, Aceptacion

class CursoAdmin(admin.ModelAdmin):
    list_display=("categoria","nombre","cupos","pendientes","autor")
    search_fields=("nombre","autor","categoria")
    list_filter=("cupos","autor","categoria","updated","created",)
    readonly_fields=("updated","created")
    date_hierarchy="updated"

class NotificacionAdmin(admin.ModelAdmin):
    list_display=("curso","descripcion")
    search_fields=("curso",)
    list_filter=("updated","created",)
    readonly_fields=("updated","created")
    date_hierarchy="updated"

class CategoriaAdmin(admin.ModelAdmin):
    list_display=("tipo",)
    search_fields=("tipo",)
    list_filter=("updated","created",)
    readonly_fields=("updated","created")
    date_hierarchy="updated"

class CursosUsuariosAdmin(admin.ModelAdmin):
    list_display=("curso","usuario")
    search_fields=("curso","usuario")
    list_filter=("curso","usuario","updated","created",)
    readonly_fields=("updated","created")
    date_hierarchy="updated"

class AeptacionAdmin(admin.ModelAdmin):
    list_display=("id","profesor","CursosUsuarios","aceptado")
    search_fields=("profesor","CursosUsuarios")
    list_filter=("profesor","CursosUsuarios","aceptado","updated","created",)
    readonly_fields=("updated","created")
    date_hierarchy="updated"

admin.site.register(Curso,CursoAdmin)
admin.site.register(Notificacion,NotificacionAdmin)
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(CursosUsuarios,CursosUsuariosAdmin)
admin.site.register(Aceptacion,AeptacionAdmin)
# Register your models here.
