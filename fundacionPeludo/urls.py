from django.contrib import admin
from django.urls import path
from django.urls.conf import include

import appPeludo.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', appPeludo.views.home, name="home"),
    path('consultaClima/', appPeludo.views.consultaClima, name="clima"),
    path('formulario/', appPeludo.views.Formulario, name="formulario"),
    path('listamascotas/', appPeludo.views.listaMascotas, name="listamascotas"),
    path('listamascotasUser/', appPeludo.views.listaMascotasUser, name="listamascotasUser"),
    path('index/', appPeludo.views.index, name="index"),
    #Guardar datos con formulario

    path('nuevaMascota/', appPeludo.views.nuevaMascota, name="nuevaMascota"),
    path('guardarMascota/', appPeludo.views.guardarMascota , name="guardarMascota"),

    #Ruta Formulario Agregar/Modificar/Eliminar

    path('formmascota/', appPeludo.views.formMascota, name="formmascota"),
    path('formmascotaMod/<int:id>/', appPeludo.views.formMascotaMod, name="formmascotaMod"),
    path('formmascotaDel/<int:id>/', appPeludo.views.formMascotaDel, name="formmascotaDel"),


    #Ruta API

    path('api/', include('webservice_mascota.urls'))
]
