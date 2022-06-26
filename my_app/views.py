import re
from django.shortcuts import render
from requests import patch
from . import models
import math
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
        print(request.POST)
    return render(request, f'{path_template}{templates_my_app[1]}', context=None)


def mar(request):

    return render(request, f'{path_template}{templates_my_app[2]}', context=None)


def colombiana(request):

    return render(request, f'{path_template}{templates_my_app[3]}', context=None)