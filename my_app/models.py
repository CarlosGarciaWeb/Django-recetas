from django.db import models

# Create your models here.

class RecetasItalianas(models.Model):
    nombre_plato = models.CharField(max_length=30, unique=True, null=False)
    tiempo_cocina = models.IntegerField(unique=False, null=False)
    ingredientes = models.CharField(max_length=100 ,unique=False, null=False)
    autor = models.CharField(max_length=30, unique=False, null=False)
    dificultad = models.IntegerField(unique=False, null=False)
    fecha_agregada = models.DateField(unique=False, null=False)

class RecetasMar(models.Model):
    nombre_plato = models.CharField(max_length=30, unique=True, null=False)
    tiempo_cocina = models.IntegerField(unique=False, null=False)
    ingredientes = models.CharField(max_length=100 ,unique=False, null=False)
    autor = models.CharField(max_length=30, unique=False, null=False)
    dificultad = models.IntegerField(unique=False, null=False)
    fecha_agregada = models.DateField(unique=False, null=False)

class RecetasColombianas(models.Model):
    nombre_plato = models.CharField(max_length=30, unique=True, null=False)
    tiempo_cocina = models.IntegerField(unique=False, null=False)
    ingredientes = models.CharField(max_length=100 ,unique=False, null=False)
    autor = models.CharField(max_length=30, unique=False, null=False)
    dificultad = models.IntegerField(unique=False, null=False)
    fecha_agregada = models.DateField(unique=False, null=False)