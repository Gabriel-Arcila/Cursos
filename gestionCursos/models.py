from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Categoria(models.Model):
    tipo = models.CharField(max_length=30)
    created =  models.DateTimeField(auto_now_add=True)
    updated =  models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'
    def __str__(self):
        return self.tipo


class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=80)
    cupos = models.IntegerField()
    pendientes = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    created =  models.DateTimeField(auto_now_add=True)
    updated =  models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='curso'
        verbose_name_plural='cursos'

    def __str__(self):
        return self.nombre

class Notificacion(models.Model):
    titulo = models.CharField(max_length=40, default="Nada")
    curso = models.ForeignKey(Curso , on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200)
    created =  models.DateTimeField(auto_now_add=True)
    updated =  models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='notificacion'
        verbose_name_plural='notificaciones'

    def __str__(self):
        return self.titulo

class CursosUsuarios(models.Model):
    curso = models.ForeignKey(Curso , on_delete=models.CASCADE)
    usuario = models.ForeignKey(User , on_delete=models.CASCADE)
    created =  models.DateTimeField(auto_now_add=True)
    updated =  models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='CursoUsuario'
        verbose_name_plural='CursosUsuarios'
    def __str__(self):
        return str(self.usuario) + '=' + str(self.curso)

class Aceptacion(models.Model):
    profesor = models.ForeignKey(User , on_delete=models.CASCADE)
    CursosUsuarios = models.ForeignKey(CursosUsuarios , on_delete=models.CASCADE)
    aceptado = models.BooleanField(default=False)
    created =  models.DateTimeField(auto_now_add=True)
    updated =  models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='Aceptado'
        verbose_name_plural='Aceptados'
    def __str__(self):
        return str(self.id)

"""class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    email = models.EmailField()
    contrasena = models.CharField(max_length=30)
    created =  models.DateTimeField(auto_now_add=True)
    updated =  models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='usuario'
        verbose_name_plural='usuarios'

    def __str__(self):
        return self.nombre
"""
