from django.urls import path
from . import views

urlpatterns = [
    path("", views.visualizarPedidos, name="visualizarPedidos"),
    path("comanda/", views.comanda, name="comanda"),
    path("pedido/<int:id>", views.pedido, name="pedido"),
    path("atualizar-pedido/<int:id>", views.atualizarPedido, name="atualizarPedido"),
    path("pesquisarMesa", views.pesquisarMesa, name="pesquisarMesa"),
]
