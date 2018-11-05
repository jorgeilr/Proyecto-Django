from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import AgregarUsuario,Login
from .models import Usuario
from django.template import loader

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
# def index(request):
#     if request.user.is_authenticated:
#         return redirect('gestionarUsuarios')
#     else:
#         return redirect('index')
def salir(request):
    logout(request)
    return redirect('/')

#
def index(request):
    plantilla=loader.get_template("index.html")
    contexto={
        'titulo':"titulo",
    }
    return HttpResponse(plantilla.render(contexto,request)) 

# def gestionarUsuarios(request):
#     form=AgregarUsuario(request.POST)
#     if form.is_valid():
#         data=form.cleaned_data
#        # regDB=User(username=data.get("username"),password=data.get("password"),email=data.get("correo"))
#         regDB=User.objects.create_user(data.get("username"),data.get("correo"),data.get("password"))
#         usuario=Usuario(user=regDB,rut=data.get("rut"),perfil=data.get("perfil"),nombre=data.get("nombre"),fechaNacimiento=data.get("fechaNacimiento"),telefono=data.get("telefono"),region=data.get("region"),ciudad=data.get("ciudad"),tipoHogar=data.get("tipoHogar"),)
#         regDB.save()
#         usuario.save()
#     usuarios=Usuario.objects.all()
#     form=AgregarUsuario()
#     return render(request,"gestionUsuario.html",{'form':form,'usuarios':usuarios,})

@login_required(login_url='login')
def gestionarUsuarios(request):
    actual=request.user
    usuarios=Usuario.objects.all()
    form=AgregarUsuario(request.POST)
    if form.is_valid():
        data=form.cleaned_data
       #regDB=User(username=data.get("username"),password=data.get("password"),email=data.get("correo"))
        regDB=User.objects.create_user(username=data.get("username"),email=data.get("correo"),password=data.get("password"))
        usuario=Usuario(user=regDB,rut=data.get("rut"),perfil=data.get("perfil"),nombre=data.get("nombre"),)
        #regDB.save()
        usuario.save()
   
    form=AgregarUsuario()
    return render(request,"gestionUsuario.html",{'actual':actual,'form':form,'usuarios':usuarios,})
@login_required(login_url='login')
def gestionMascota(request):
    form = AgregarMascota(request.POST)
    if form.is_valid():
        data=form.cleaned_data
        redDB=Mascota(fichaMascota=data.get("fichaMascota"),nombreMascota=data.get("nombreMascota"),razaMascota=data.get("razaMascota"),)     
        regDB.save() 
    form = AgregarMascota()
    mascotas=Mascota.objects.all()
    titulo="Gestion Mascotas"
    return render(request,"ingresarMascota.html",{'mascotas':mascotas,'form':form,'titulo':titulo,})

def ingresar(request):
    form=Login(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
        user=authenticate(username=data.get("username"),password=data.get("password"))
        if user is not None:
            login(request,user)
            return redirect('gestionUsuario')
        
    return render(request,"login.html",{'form':form,})