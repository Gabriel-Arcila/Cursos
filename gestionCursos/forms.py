from django import forms
from django.contrib.auth.models import User
from .models import Curso, Notificacion, Post, P1T1I, P2T1I, P1T1V, P2T2I, P3T1I

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

class FormPOST(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["titulo","curso"]

class FormP1T1I(forms.ModelForm):
    class Meta:
        model = P1T1I
        fields = ['Post',"texto1","img1"]

class FormP2T1I(forms.ModelForm):
    class Meta:
        model = P2T1I
        fields = ['Post',"texto1","texto2","img1"]

class FormP1T1V(forms.ModelForm):
    class Meta:
        model = P1T1V
        fields = ['Post',"texto1","vid1"]

class FormP2T2I(forms.ModelForm):
    class Meta:
        model = P2T2I
        fields = ['Post',"texto1","texto2","img1","img2"]

class FormP3T1I(forms.ModelForm):
    class Meta:
        model = P3T1I
        fields = ['Post',"texto1","texto2","texto3","img1"]
