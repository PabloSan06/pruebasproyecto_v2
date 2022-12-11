from audioop import reverse
from datetime import datetime
from django.shortcuts import redirect, render
from django.conf import settings
from .forms import ContactoForm
from django.http import HttpResponseRedirect
from django.contrib import messages


def index(request):
    saludos = ['Hola', 'Hello', 'Olá', "Buenas"]
    idioma_saludo = {'en': 'Hello', 'es': 'Hola', 'br': 'Olá'}
    return render(request, "hola_mundo/index.html", {"hoy": datetime.now, "saludos": saludos, "idioma_saludos": idioma_saludo})


def clientes(request):
    tipClie = ['IA', 'Marketing', 'Llamado', 'Portales']
    return render(request, "hola_mundo/clientes.html", {"clientes": tipClie})


def contacto(request):
    if request.method == "POST":
        # Creao la instancia populada con los datos cargados en pantalla
        contacto_form = ContactoForm(request.POST)
        # Valido y proceso los datos.
        if contacto_form.is_valid():
            messages.set_level(request, messages.DEBUG)
            messages.success(request, "Formulario cargado Correctamente")
            messages.debug(request, "Debuggeando")
            messages.info(request, "Información importante")
            messages.warning(request, "Cuidado lobo suelto")
            messages.error(request, "No funciona")
    else:
        # Creo el formulario vacío con los valores por defecto
        contacto_form = ContactoForm()
    return render(request, "hola_mundo/contacto.html", {'contacto_form': contacto_form})

def actcont(request):
    
    return render(request, "hola_mundo/actcont.html")

def infemp(request):
    
    return render(request, "hola_mundo/infemp.html")