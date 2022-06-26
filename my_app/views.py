import re
from django.shortcuts import render, redirect
from django.urls import reverse
from requests import patch
from . import models
from datetime import date
# Create your views here.


path_template = 'my_app/'

templates_my_app = ['index.html', 'italiana.html', 'mar.html', 'colombiana.html']

## Render Templates

def home(request):
    recetas_italianas = models.RecetasItalianas.objects.all()
    recetas_mar = models.RecetasMar.objects.all()
    recetas_colombianas = models.RecetasColombianas.objects.all()
    context = {
        'italianas': recetas_italianas,
        'mar': recetas_mar,
        'colombianas': recetas_colombianas
    }
    return render(request, f'{path_template}{templates_my_app[0]}', context=context)




def italiana(request):
    
    # Test POST
    if request.POST:
        today = date.today()
        receta = request.POST['receta']
        duracion = int(request.POST['tiempo'])
        ingredientes = request.POST['ingredientes']
        autor = request.POST['autor']
        dificultad = int(request.POST['dificultad'])
        print(today, receta, duracion, ingredientes, autor, dificultad)
        models.RecetasItalianas.objects.create(nombre_plato=receta, tiempo_cocina=duracion, ingredientes=ingredientes, autor=autor, dificultad=dificultad, fecha_agregada=today)
        return redirect(reverse('my_app:home'))
    return render(request, f'{path_template}{templates_my_app[1]}', context=None)


def mar(request):
    if request.POST:
        today = date.today()
        receta = request.POST['receta']
        duracion = int(request.POST['tiempo'])
        ingredientes = request.POST['ingredientes']
        autor = request.POST['autor']
        dificultad = int(request.POST['dificultad'])
        print(today, receta, duracion, ingredientes, autor, dificultad)
        models.RecetasMar.objects.create(nombre_plato=receta, tiempo_cocina=duracion, ingredientes=ingredientes, autor=autor, dificultad=dificultad, fecha_agregada=today)
        return redirect(reverse('my_app:home'))
    return render(request, f'{path_template}{templates_my_app[2]}', context=None)


def colombiana(request):
    if request.POST:
        today = date.today()
        receta = request.POST['receta']
        duracion = int(request.POST['tiempo'])
        ingredientes = request.POST['ingredientes']
        autor = request.POST['autor']
        dificultad = int(request.POST['dificultad'])
        print(today, receta, duracion, ingredientes, autor, dificultad)
        models.RecetasColombianas.objects.create(nombre_plato=receta, tiempo_cocina=duracion, ingredientes=ingredientes, autor=autor, dificultad=dificultad, fecha_agregada=today)
        return redirect(reverse('my_app:home'))
    return render(request, f'{path_template}{templates_my_app[3]}', context=None)