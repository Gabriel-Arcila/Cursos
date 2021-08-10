from django.contrib.auth.views import PasswordChangeDoneView
from django.shortcuts import render, HttpResponse, redirect
from gestionCursos.models import Curso, Categoria, CursosUsuarios, Notificacion, Aceptacion, Post, P1T1I, P3T1I, P2T2I, P2T1I, P1T1V
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .forms import FormCurso, FormNotificaciones, FormPOST

# Create your views here.
"""def lista_cursos(request):
    lista= Cursos.objects.all()
    return render(request, "listaCursosPersona.html", {"lista":lista})

def lista_cursosN(request):
    return render(request, "listaCursosPrincipiante.html")"""

def registrar(request):
    band = False
    if request.method == "POST":
        contrasena=request.POST.get("password")
        email=request.POST.get("email")
        nombre=request.POST.get("username")
        if nombre.strip() == ' ' or email.strip() ==' ' or contrasena.strip() ==' ':
            band = True
            dato = "Ningun dato puede estar vacio"
            return render(request,"gestionCursos/registro.html",{'band':band,'dato':dato})
        elif len(contrasena) < 8:
            band = True
            dato = "La clave tiene que tener al menos 8 caracteres"
            return render(request,"gestionCursos/registro.html",{'band':band,'dato':dato})
        else:
            contrasena = make_password(contrasena)
            nuevo = User(email=email,username=nombre,password=contrasena)
            nuevo.save()
            return redirect('inicio')
        """
        nuevo = UserForm(request.POST)
        if nuevo.is_valid():
            nuevo.save()
        """
    return render(request,"gestionCursos/registro.html",{'band':band})

def inicioUsuario(request):
    return render(request,"gestionCursos/home.html")

def notificaciones(request,user_id):
    lista=[]
    cursosUsuario = CursosUsuarios.objects.filter(usuario=user_id)
    for dato in cursosUsuario:
        print(dato.curso.id)
    for elemento in cursosUsuario:
        dato = Aceptacion.objects.get(CursosUsuarios=elemento)
        if dato.aceptado:
            Notificaciones = Notificacion.objects.filter(curso=elemento.curso.id)
            print(Notificaciones)
            lista.append(Notificaciones)
    print(lista)
    return render(request,"gestionCursos/notificacion.html",{"lista":lista})

def lista(request):
    cursos= Curso.objects.all()
    categorias= Categoria.objects.all()
    return render(request,"gestionCursos/listaCompleta.html",{"cursos": cursos,"categorias":categorias})

def listaUsuario(request,user_id):
    user_id = int(user_id)
    if request.method == "POST":
        id_curso = int(request.POST.get("id"))
        insC = Curso.objects.filter(id=id_curso)
        insU = User.objects.filter(id=user_id)
        compro = CursosUsuarios.objects.all()
        for elemento in compro:
            if elemento.usuario == insU.get() and elemento.curso == insC.get():
                break
        else:
            nuevo = CursosUsuarios(usuario=insU.get(), curso=insC.get())
            nuevo.save()

            profesor = insC.get().autor
            nuevo2 = Aceptacion(CursosUsuarios=nuevo, aceptado=False, profesor=profesor)
            nuevo2.save()

            nuevo = insC.get()
            #?nuevo.cupos -= 1
            nuevo.pendientes += 1
            nuevo.save()
    lista=[]
    cursosUsuario = CursosUsuarios.objects.filter(usuario=user_id)
    for elemento in cursosUsuario:
        acepta = Aceptacion.objects.get(CursosUsuarios=elemento)
        if acepta.aceptado == True:
            curso = Curso.objects.filter(id=elemento.curso.id)
            lista.append(curso)
    return render(request,"gestionCursos/listaUsuario.html",{"lista":lista,})

def contacto(request):
    return render(request,"gestionCursos/contacto.html")

def categoria(request, categoria_id):
    categoria_id = int(categoria_id)
    #categorias = Categoria.objects.get(id=categoria_id)
    cursos = Curso.objects.filter(categoria=categoria_id)
    categorias= Categoria.objects.all()
    return render(request,"gestionCursos/categoria.html",{'categorias': categorias, 'cursos': cursos})

def agragarCurso(request):
    if request.method == "POST":
        #print(request.POST.get['id'])
        return render(request,"gestionCursos/contacto.html")

def formularioCursos(request):
    band = False
    categoria = Categoria.objects.all()
    if request.method == "POST":
        form = FormCurso(request.POST)
        if form.is_valid():
                form.save()
        else:
            band = True
            error = 'Datos muy grandes'
            return render(request,"gestionCursos/formularioCursos.html",{"lista":categoria,"band":band,'error':error})
    return render(request,"gestionCursos/formularioCursos.html",{"lista":categoria,"band":band})

def formularioNotificaciones(request,id):
    id = int(id)
    band = False
    profesor = User.objects.get(id=id)
    cursos = Curso.objects.filter(autor=profesor)
    if request.method == "POST":
        id = int(request.POST.get("id"))
        profesor = User.objects.get(id=id)
        cursos = Curso.objects.filter(autor=profesor)
        for curso in cursos:
            if int(request.POST.get("curso")) == curso.id:
                break
        else:
            band = True
            error = 'No posees este curso'
            return render(request,"gestionCursos/formularioNotificaciones.html",{"lista":cursos,"band":band,'error':error})
        form = FormNotificaciones(request.POST)
        if form.is_valid():
            form.save()
        else:
            band = True
            error = 'Datos muy grandes'
            return render(request,"gestionCursos/formularioNotificaciones.html",{"lista":cursos,"band":band,'error':error})
    return render(request,"gestionCursos/formularioNotificaciones.html",{"lista":cursos,"band":band})

""" form = FormP1T1I(request.POST)
    if request.method == "POST":
        if form.is_valid():
            print(request.FILES.get('img1'))
            return render(request,"gestionCursos/nada.html",{"lista":form})
        print(request.FILES.get('img1'))
        print('llego aqui'
    return render(request,"gestionCursos/nada.html",{"lista":form})
"""

def formularioPost(request, id):
    if request.method == "POST":
        if request.POST.get('Post') != None:
            plantilla = int(request.POST.get('plantilla'))
            if plantilla == 0:
                text1 = request.POST.get('texto1')
                im1 = request.FILES.get('img1')
                pot = request.POST.get('Post')
                pot = Post.objects.get(id=int(pot))
                print(text1,im1,pot)
                plan = P1T1I(texto1 = text1, img1 = im1, Post = pot);
                """form = FormP1T1I(request.POST)
                print("entro FormP1T1I")
                print(request.POST.get('img1'))
                return render(request,"gestionCursos/nada.html",{"lista":form})
                print("entro FormP1T1I")"""
            elif plantilla == 1:
                text1 = request.POST.get('texto1')
                text2 = request.POST.get('texto2')
                text3 = request.POST.get('texto3')
                im1 = request.FILES.get('img1')
                pot = request.POST.get('Post')
                pot = Post.objects.get(id=int(pot))
                plan = P3T1I(texto1 = text1,texto2 = text2,texto3 = text3, img1 = im1, Post = pot);
            elif plantilla == 2:
                text1 = request.POST.get('texto1')
                text2 = request.POST.get('texto2')
                im1 = request.FILES.get('img1')
                im2 = request.FILES.get('img2')
                pot = request.POST.get('Post')
                pot = Post.objects.get(id=int(pot))
                plan = P2T2I(texto1 = text1, texto2 = text2, img1 = im1, img2 = im2,Post = pot);
            elif plantilla == 3:
                text1 = request.POST.get('texto1')
                text2 = request.POST.get('texto2')
                im1 = request.FILES.get('img1')
                pot = request.POST.get('Post')
                pot = Post.objects.get(id=int(pot))
                plan = P2T1I(texto1 = text1, texto2 = text2, img1 = im1,Post = pot);
            elif plantilla == 4:
                print('entro')
                text1 = request.POST.get('texto1')
                vid1 = request.POST.get('vid1')
                print(vid1)
                pot = request.POST.get('Post')
                pot = Post.objects.get(id=int(pot))
                plan = P1T1V(texto1 = text1, vid1 = vid1, Post = pot);
            plan.save()
            profesor = User.objects.get(id=id)
            cursos = Curso.objects.filter(autor=profesor)
            return render(request,"gestionCursos/formularioPost.html",{"lista":cursos})
        else:
            form = FormPOST(request.POST)
            if form.is_valid():
                #form.save()
                print(request.POST.get('plantilla'))
                print('aqui')
                vec=Post.objects.all()
                num =  vec[len(vec)-1]
                post = Post.objects.get(id=num.id)
                return render(request,"gestionCursos/Plantillas.html",{'plantilla':int(request.POST.get('plantilla')),"post":post})
            else:
                profesor = User.objects.get(id=id)
                cursos = Curso.objects.filter(autor=profesor)
                band = True
                error = 'Datos muy grandes'
                return render(request,"gestionCursos/formularioPost.html",{"lista":cursos,"band":band,'error':error})
    band = False
    profesor = User.objects.get(id=id)
    cursos = Curso.objects.filter(autor=profesor)
    return render(request,"gestionCursos/formularioPost.html",{"lista":cursos})

def aceptarNotificaciones(request, id):
    if request.method == "POST":
        idU = int(request.POST.get("idA"))
        ok = bool (request.POST.get("ok"))
        Aceptar = Aceptacion.objects.get(id=idU)
        if ok != True:
            ok = False
        if ok !=  Aceptar.aceptado:
            if ok:
                Aceptar.aceptado = True
                dato = Aceptar.CursosUsuarios.curso.id
                curso = Curso.objects.get(id=dato)
                curso.pendientes = curso.pendientes -1
                curso.cupos = curso.cupos - 1
            else:
                Aceptar.aceptado = False
                dato = Aceptar.CursosUsuarios.curso.id
                curso = Curso.objects.get(id=dato)
                curso.pendientes = curso.pendientes + 1
                curso.cupos = curso.cupos + 1
            Aceptar.save()
            curso.save()
    profesor = User.objects.get(id=int(id))
    aceptado = Aceptacion.objects.filter(profesor=profesor)
    return render(request,"gestionCursos/AceptarNotificaciones.html",{"lista":aceptado})