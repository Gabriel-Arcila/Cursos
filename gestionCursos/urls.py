from django.urls import path
from django.contrib.auth.views import login_required
from gestionCursos import  views

urlpatterns = [
    path('inicio/', login_required(views.inicioUsuario), name="inicio de usuario"),
    path('notificaciones/<user_id>', login_required(views.notificaciones), name="notificaciones"),
    path('lista/', login_required(views.lista), name="lista"),
    path('listaUsuario/<user_id>', login_required(views.listaUsuario), name="lista de usuario"),
    path('contacto/', login_required(views.contacto), name="contacto"),
    path('categoria/<categoria_id>', login_required(views.categoria), name="categoria"),
    path('formularioCursos/', login_required(views.formularioCursos), name="formularioCursos"),
    path('formularioPost/<int:id>', login_required(views.formularioPost), name="formularioPost"),
    path('formularioNotificaciones/<id>', login_required(views.formularioNotificaciones), name="formularioNotificaciones"),
    path('aceptarNotificaciones/<id>', login_required(views.aceptarNotificaciones), name="aceptarNotificaciones"),
]

