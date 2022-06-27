from locale import format_string
from django.shortcuts import render, redirect
from django.urls import reverse
from requests import patch
from . import models
from .forms import RecetaItalianaForm, RecetaMarForm, RecetaColombianaForm, BuscarForm

# Create your views here.


path_template = 'my_app/'

templates_my_app = ['index.html', 'italiana.html', 'mar.html', 'colombiana.html']

## Render Templates

def home(request):
    recetas_italianas = models.RecetasItalianas.objects.all()
    cantidad_recetas_italianas = len(recetas_italianas)
    inicio_italianas = 0
    if cantidad_recetas_italianas > 5:
        inicio_italianas =  cantidad_recetas_italianas - 5
    recetas_mar = models.RecetasMar.objects.all()
    cantidad_recetas_mar = len(recetas_mar)
    inicio_mar = 0
    if cantidad_recetas_mar > 5:
        inicio_mar = cantidad_recetas_mar - 5
    recetas_colombianas = models.RecetasColombianas.objects.all()
    cantidad_recetas_colombianas = len(recetas_colombianas)
    inicio_colombianas = 0
    if cantidad_recetas_colombianas > 5:
        inicio_colombianas = cantidad_recetas_colombianas - 5
    context = {
        'italianas': recetas_italianas[inicio_italianas: cantidad_recetas_italianas],
        'mar': recetas_mar[inicio_mar: cantidad_recetas_mar],
        'colombianas': recetas_colombianas[inicio_colombianas: cantidad_recetas_colombianas]
    }
    return render(request, f'{path_template}{templates_my_app[0]}', context=context)




def italiana(request):
    # Test POST
    recetas_italianas = models.RecetasItalianas.objects.all()
    if request.method == 'POST':
        if request.POST.get('nombre_receta'):
            busqueda = request.POST['nombre_receta']
            forms = RecetaItalianaForm()
            recetas = models.RecetasItalianas.objects.filter(nombre_plato__contains=busqueda)
            resultados = len(recetas)
            return render(request, f'{path_template}{templates_my_app[1]}', context={'forms': forms, 'busqueda': recetas, 'resultado':resultados, 'receta_buscada': busqueda, 'italianas': recetas_italianas})
        else:
            forms = RecetaItalianaForm(request.POST)
            if forms.is_valid():
                forms.save()
                return redirect(reverse('my_app:home'))
    else:
        forms = RecetaItalianaForm()
    return render(request, f'{path_template}{templates_my_app[1]}', context={'forms': forms, 'italianas': recetas_italianas})


def mar(request):
    recetas_mar = models.RecetasMar.objects.all()
    if request.method == 'POST':
        if request.POST.get('nombre_receta'):
            busqueda = request.POST['nombre_receta']
            forms = RecetaMarForm()
            recetas = models.RecetasMar.objects.filter(nombre_plato__contains=busqueda)
            resultados = len(recetas)
            return render(request, f'{path_template}{templates_my_app[2]}', context={'forms': forms, 'busqueda': recetas, 'resultado': resultados, 'receta_buscada': busqueda, 'mar': recetas_mar})
        else:
            forms = RecetaMarForm(request.POST)
            if forms.is_valid():
                forms.save()
                return redirect(reverse('my_app:home'))
    else:
        forms = RecetaMarForm()
    return render(request, f'{path_template}{templates_my_app[2]}', context={'forms':forms, 'mar': recetas_mar})


def colombiana(request):
    recetas_colombianas = models.RecetasColombianas.objects.all()
    if request.method == 'POST':
        if request.POST.get('nombre_receta'):
            busqueda = request.POST['nombre_receta']
            forms = RecetaColombianaForm()
            recetas = models.RecetasColombianas.objects.filter(nombre_plato__contains=busqueda)
            resultados = len(recetas)
            return render(request, f'{path_template}{templates_my_app[3]}', context={'forms': forms, 'busqueda': recetas, 'resultado': resultados, 'receta_buscata': busqueda, 'colombianas': recetas_colombianas})
        else:
            forms = RecetaColombianaForm(request.POST)
            if forms.is_valid():
                forms.save()
                return redirect(reverse('my_app:home'))

    else:
        forms = RecetaColombianaForm()
    return render(request, f'{path_template}{templates_my_app[3]}', context={'forms':forms, 'colombianas': recetas_colombianas})