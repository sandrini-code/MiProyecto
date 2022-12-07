import datetime

from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render

#Request: Para realizar peticiones
#HttpResponse: Para enviar la respuesta usando el protocolo HTTP

#esto es una vista
def bienvenida(request): #pasamos un objeto de tipo request como primer argumento
    return HttpResponse("bienvenido a django. =")

def bienvenidaRojo(request): #pasamos un objeto de tipo request como primer argumento
    return HttpResponse("<p style='color: red;'>bienvenido a django. =)</p>")
def categoria_edad(request, edad):

    if edad >= 18:
        if edad>=60:
            categoria="tercera edad"
        else:
            categoria="adultez"
    else:
        if edad<10:
            categoria="infancia"
        else:
            categoria="adolescencia"
    resultado= f"<h1>categoria de la edad: {categoria} </h1>"
    #resultado=edad
    return HttpResponse(resultado)

def contenido_Html(request, nombre, edad):
    contenido=f"""
    <html>
    <body>
    <p>Nombre: {nombre} / Edad: {edad}</p>
    </body>
    </html>
    """ #% (nombre, edad)
    return HttpResponse(contenido)

def contenido_Html2(request):
    contenido="""
    <html>
	<head>
	<title>Mi página de ejemplo</title>
	</head>
	<body>
	Aquí va el contenido
	<a href="https://mx.godaddy.com/blog">Visita el blog de GoDaddy</a>
	<img src="https://images.unsplash.com/photo-1535378917042-10a22c95931a">
	</body>
	</html>
    """ #% (nombre, edad)
    return HttpResponse(contenido)

def miPrimeraPlantilla(request):
    #abrimos el documento que contiene la plantilla
    plantillaExterna= open("C:/MiProyecto/MiProyecto/plantillas/MiPrimeraPlantilla.html")
    #cargar el documento en una variable de tipo Template
    template= Template(plantillaExterna.read())
    #Cerrar el documento externo que hemos abierto
    plantillaExterna.close()
    #crear un contexto
    contexto= Context()
    #Renderizar el documento
    documento= template.render(contexto)
    return HttpResponse(documento)

def plantillaParametros1(request):
    nombre="pedro"
    apellido="ramirez"
    fechaActual= datetime.datetime.now()
    lenguajes=["PYTHON", "ruby", "JAVA", "c#", "kolin"]
    #abrimos el documento que contiene la plantilla
    plantillaExterna= open("C:/MiProyecto/MiProyecto/plantillas/plantillaParametros1.html")
    #cargar el documento en una variable de tipo Template
    template= Template(plantillaExterna.read())
    #Cerrar el documento externo que hemos abierto
    plantillaExterna.close()
    #crear un contexto
    contexto= Context({"miNombre":nombre, "apellido":apellido, "fechaActual": fechaActual, "lenguajes": lenguajes})
    #Renderizar el documento
    documento= template.render(contexto)
    return HttpResponse(documento)

def plantillaCargador(request):
    nombre = "pedro"
    apellido = "ramirez"
    fechaActual = datetime.datetime.now()
    lenguajes = ["PYTHON", "PHP","ruby", "JAVA", "c#", "kolin"]
    plantillaExterna= loader.get_template("plantillaParametros1.html")
    documento= plantillaExterna.render({"miNombre":nombre, "apellido":apellido, "fechaActual": fechaActual, "lenguajes": lenguajes})
    return HttpResponse(documento)

def plantillaShortcut(request):
    nombre = "pedro"
    apellido = "ramirez"
    fechaActual = datetime.datetime.now()
    lenguajes = ["PYTHON", "PHP","ruby", "JAVA", "c#", "kolin", "c++"]

    return render(request,"plantillaParametros1.html",  {"miNombre":nombre, "apellido":apellido, "fechaActual": fechaActual, "lenguajes": lenguajes})

def plantillaHija1(request):
    return render(request, "plantillaHija1.html", {})

def plantillaHija2(request):
    return render(request, "plantillaHija2.html", {})
def blog(request):
    return render(request, "blog.html", {})
def quienesSomos(request):
    return render(request, "quienesSomos.html", {})