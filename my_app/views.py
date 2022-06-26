from locale import format_string
from django.shortcuts import render, redirect
from django.urls import reverse
from requests import patch
from . import models
from .forms import RecetaItalianaForm, RecetaMarForm, RecetaColombianaForm

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
    if request.method == 'POST':
        forms = RecetaItalianaForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect(reverse('my_app:home'))
    else:
        forms = RecetaItalianaForm()
    return render(request, f'{path_template}{templates_my_app[1]}', context={'forms': forms})


def mar(request):
    if request.method == 'POST':
        forms = RecetaMarForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect(reverse('my_app:home'))
    else:
        forms = RecetaMarForm()
    return render(request, f'{path_template}{templates_my_app[2]}', context={'forms':forms})


def colombiana(request):
    if request.method == 'POST':
        forms = RecetaColombianaForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect(reverse('my_app:home'))

    else:
        forms = RecetaColombianaForm()
    return render(request, f'{path_template}{templates_my_app[3]}', context={'forms':forms})