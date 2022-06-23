from django.urls import path
from . import views

app_name = 'my_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('recetas-italiana/', views.italiana, name='italiana'),
    path('recetas-mar/', views.mar, name='mar'),
    path('recetas-colombiana/', views.colombiana, name='colombiana'),
]