from django.shortcuts import render
from .models import Familia
from django.http import HttpResponse
from django.template import loader
import datetime
# Create your views here.


def crearfamiliar(request):
    
    familiar = Familia(nombre="Lucas", edad=48, fecha=datetime.datetime.now())
    familiar.save()
    fecha=datetime.datetime.today()
    nuevofamiliar=f"Nuevo familiar: {familiar.nombre}, con una edad de :{familiar.edad}, Hoy es {fecha}"
    template = loader.get_template("familiatemplate.html")
    nuevofamiliar = template.render(familiar)

    return HttpResponse (nuevofamiliar)


def familiareshtml(request):
    familiares = {"nombre":"Lucas","edad":42, "fecha":datetime.datetime.today}
    template = loader.get_template("familiatemplate.html")
    nuevofamiliar = template.render(familiares)
    return HttpResponse(nuevofamiliar)


    template = loader.get_template("familiatemplate.html")
    nuevofamiliar = template.render(familiar)