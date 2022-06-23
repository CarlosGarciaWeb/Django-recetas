from django.shortcuts import render
from requests import patch

# Create your views here.


path_template = 'my_app/'

templates_my_app = ['index.html', 'italiana.html', 'mar.html', 'colombiana.html']

## Render Templates

def home(request):
    return render(request, f'{path_template}{templates_my_app[0]}')




def italiana(request):
    return render(request, f'{path_template}{templates_my_app[1]}')


def mar(request):
    return render(request, f'{path_template}{templates_my_app[2]}')


def colombiana(request):
    return render(request, f'{path_template}{templates_my_app[3]}')