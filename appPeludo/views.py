from appPeludo.forms import MascotasForm
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from appPeludo.models import Mascotas

#Clases de ejemplo
# Create your views here.

def home(request):
    return render(request,'index.html')

def consultaClima(request):
    return render(request,'consultaClima.html')

def Formulario(request):
    return render(request,'formulario.html')

def index(request):
    return render(request,'index2.html')

def listaMascotas(request):
    mascotas = Mascotas.objects.all()

    return render(request, 'listamascotas.html', {'mascotas':mascotas})

def listaMascotasUser(request):
    mascotas = Mascotas.objects.all()

    return render(request, 'listamascotasUser.html', {'mascotas':mascotas})

def nuevaMascota(request):
    return render(request,'nuevaMascota.html')

def guardarMascota(request):

    codigo = request.POST['codigo']
    nombre = request.POST['nombre']

    mascota = Mascotas(
        codigo = codigo,
        nombre = nombre,
        especie = "",
        adoptado = 0
    )

    mascota.save()

    return redirect('listamascotas')

def formMascota(request):
    datos = {
        'form' : MascotasForm()
    }
    if request.method=='POST' :
        formulario  = MascotasForm(request.POST)

        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Datos guardados correctamente"

    return render(request, 'nuevaMascotaForm.html', datos)

def formMascotaMod(request, id):
    mascota = Mascotas.objects.get(id=id)
    datos = {
        'form' : MascotasForm(instance=mascota)
    }
    if request.method=='POST' :
        formulario  = MascotasForm(data=request.POST, instance=mascota)

        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Datos modificados correctamente"

    return render(request, 'editarMascotaForm.html', datos)

def formMascotaDel(request, id):
    mascota = Mascotas.objects.get(id=id)
    mascota.delete()

    datos = {
        'form' : MascotasForm(instance=mascota)
    }
    
    return redirect('listamascotasUser')
