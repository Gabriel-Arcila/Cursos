from django import forms
from django.contrib.auth.models import User
from .models import Curso, Notificacion

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email','username','password']

class FormCurso(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ["nombre","descripcion","cupos","categoria","autor"]

class FormNotificaciones(forms.ModelForm):
    class Meta:
        model = Notificacion
        fields = ["titulo","descripcion","curso"]