from xml.etree.ElementInclude import include
from django import forms
from .models import RecetasColombianas, RecetasItalianas, RecetasMar
from django.forms import ModelForm
from datetime import date


today = date.today()


class BuscarForm(forms.Form):
    nombre_plato = forms.CharField(label='Nombre de Receta')

class RecetaItalianaForm(ModelForm):

    fecha_agregada = forms.DateField(widget=forms.HiddenInput(), initial=today, label='')
    
    class Meta:
        
        model = RecetasItalianas
        fields = '__all__'
        labels = {
            'nombre_plato': 'Nombre de la receta',
            'tiempo_cocina': 'Tiempo para cocinar (ingresar numeros enteros en minutos 15-60)',
            'ingredientes': 'Ingredientes (separar por coma)',
            'autor': 'Autor (escribe tu nombre)',
            'dificultad': 'Dificultad (ingresar numeros enteros del 1-5)',
            'fecha_agregada': None,
        }




class RecetaMarForm(ModelForm):

    fecha_agregada = forms.DateField(widget=forms.HiddenInput(), initial=today, label='')

    class Meta:
        
        model = RecetasMar
        fields = '__all__'
        labels = {
            'nombre_plato': 'Nombre de la receta',
            'tiempo_cocina': 'Tiempo para cocinar (ingresar numeros enteros en minutos 15-60)',
            'ingredientes': 'Ingredientes (separar por coma)',
            'autor': 'Autor (escribe tu nombre)',
            'dificultad': 'Dificultad (ingresar numeros enteros del 1-5)',
            'fecha_agregada': None,
        }





class RecetaColombianaForm(ModelForm):

    fecha_agregada = forms.DateField(widget=forms.HiddenInput(), initial=today, label='')

    class Meta:
        
        model = RecetasColombianas
        fields = '__all__'
        labels = {
            'nombre_plato': 'Nombre de la receta',
            'tiempo_cocina': 'Tiempo para cocinar (ingresar numeros enteros en minutos 15-60)',
            'ingredientes': 'Ingredientes (separar por coma)',
            'autor': 'Autor (escribe tu nombre)',
            'dificultad': 'Dificultad (ingresar numeros enteros del 1-5)',
            'fecha_agregada': None,
        }

