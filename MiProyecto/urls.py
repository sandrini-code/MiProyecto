"""MiProyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MiProyecto.view import bienvenida, bienvenidaRojo
from MiProyecto.view import categoria_edad
from MiProyecto.view import contenido_Html, contenido_Html2
from MiProyecto.view import miPrimeraPlantilla, plantillaParametros1, plantillaCargador
from MiProyecto.view import plantillaShortcut, plantillaHija1, plantillaHija2, blog, quienesSomos

urlpatterns = [
    path('admin/', admin.site.urls),
    path("bienvenida/", bienvenida),
    path("pajaro/", bienvenidaRojo), #url y llamado a la funcion que queremos que se ejecute
    path("categoriaEdad/<int:edad>", categoria_edad),
    path("contenido_Html/<nombre>/<int:edad>", contenido_Html),
    path("contenido_Html2/", contenido_Html2),
    path("miPrimeraPlantilla/", miPrimeraPlantilla),
    path("plantillaPrametros1/", plantillaParametros1),
    path("plantillaCargador/", plantillaCargador),
    path("plantillaShortcut/", plantillaShortcut),
    path("plantillaHija1/", plantillaHija1),
    path("plantillaHija2/", plantillaHija2),
    path("", blog),
    path("quienesSomos/", quienesSomos)
    
]
