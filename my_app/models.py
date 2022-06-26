from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class RecetasItalianas(models.Model):
    nombre_plato = models.CharField(max_length=30, unique=True, null=False)
    tiempo_cocina = models.IntegerField(unique=False, null=False, validators=[MinValueValidator(15), MaxValueValidator(60)])
    ingredientes = models.CharField(max_length=100 ,unique=False, null=False)
    autor = models.CharField(max_length=30, unique=False, null=False)
    dificultad = models.IntegerField(unique=False, null=False, validators=[MinValueValidator(1), MaxValueValidator(5)])
    fecha_agregada = models.DateField(unique=False, null=False)

    def __str__(self):
        return f"{self.nombre_plato}, {self.ingredientes}, {self.autor}, {self.dificultad}, {self.fecha_agregada}"
    

    def __int__(self):
        return f"{self.tiempo_cocina}"

class RecetasMar(models.Model):
    nombre_plato = models.CharField(max_length=30, unique=True, null=False)
    tiempo_cocina = models.IntegerField(unique=False, null=False, validators=[MinValueValidator(15), MaxValueValidator(60)])
    ingredientes = models.CharField(max_length=100 ,unique=False, null=False)
    autor = models.CharField(max_length=30, unique=False, null=False)
    dificultad = models.IntegerField(unique=False, null=False, validators=[MinValueValidator(1), MaxValueValidator(5)])
    fecha_agregada = models.DateField(unique=False, null=False)

    def __str__(self):
        return f"{self.nombre_plato} , {self.ingredientes}, {self.autor}, {self.dificultad}, {self.fecha_agregada}"

    def __int__(self):
        return f"{self.tiempo_cocina}"

class RecetasColombianas(models.Model):
    nombre_plato = models.CharField(max_length=30, unique=True, null=False)
    tiempo_cocina = models.IntegerField(unique=False, null=False, validators=[MinValueValidator(15), MaxValueValidator(60)])
    ingredientes = models.CharField(max_length=100 ,unique=False, null=False)
    autor = models.CharField(max_length=30, unique=False, null=False)
    dificultad = models.IntegerField(unique=False, null=False, validators=[MinValueValidator(1), MaxValueValidator(5)])
    fecha_agregada = models.DateField(unique=False, null=False)

    def __str__(self):
        return f"{self.nombre_plato}, {self.ingredientes}, {self.autor}, {self.dificultad}, {self.fecha_agregada}"

    def __int__(self):
        return f"{self.tiempo_cocina}"