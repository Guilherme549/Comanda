from django.urls import path
from . import views

urlpatterns = [
    path("", views.visualizarPedidos, name="visualizarPedidos"),
    path("comanda/", views.comanda, name="comanda"),
    path("pedido/<int:id>", views.pedido, name="pedido"),
]
