from django.urls import path
from . import views

urlpatterns = [
    path('', views.visualizarPedidos, name="visualizarPedidos"),
    path('comanda/', views.comanda, name="comanda"),
]
