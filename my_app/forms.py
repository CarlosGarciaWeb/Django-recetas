from django import forms


class RecetaForm(forms.Form):
    receta = forms.CharField(label='Nombre de la Receta:', max_length=30)
    tiempo = forms.IntegerField(label='Tiempo total de cocina (en minutos):', min_value=15, max_value=60)
    ingredientes = forms.CharField(label='Ingredientes (separados por coma):')
    autor = forms.CharField(label='Autor:')
    dificultad = forms.IntegerField(label='Dificultas (Numeros enteros del 1 al 5):', max_value=5, min_value=1)

