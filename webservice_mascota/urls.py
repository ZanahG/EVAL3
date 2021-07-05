from django.conf.urls import url
from django.urls import path
from webservice_mascota.views import lista_mascotas, detalle_mascota
from webservice_mascota.viewsLogin import login

urlpatterns = [
    path('lista_mascotas',lista_mascotas, name="lista_mascotas"),
    path('detalle_mascota/<str:codigo>/', detalle_mascota, name="detalle_mascotas"),
    path('login', login, name="login"),
]




