from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('recetas-italiana/', views.italiana),
    path('recetas-mar/', views.mar),
    path('recetas-colombiana/', views.colombiana),
]