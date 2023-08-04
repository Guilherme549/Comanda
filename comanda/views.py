from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from .models import Comanda
import json


def visualizarPedidos(request):
    pedidos = Comanda.objects.all()
    return render(request, "index.html", {"pedidos": pedidos})


def comanda(request):
    if request.method == "GET":
        return render(request, "pedido.html")
    elif request.method == "POST":
        mesa = request.POST.get("mesa")
        cerveja = request.POST.get("cerveja")
        qtdCerveja = int(request.POST.get("qtdCerveja"))
        refrigerante = request.POST.get("refrigerantes")
        qtdRefrigerante = int(request.POST.get("qtdRefrigerante"))
        espetinho = request.POST.get("espetinhos")
        qtdEspetinho = int(request.POST.get("qtdEspetinho"))
        precoTotal = request.POST.get("precoTotal")

        listaSaboresBackend = request.POST.get("listaSaboresBackend")

        # convertendo json
        lista_sabores_backend = json.loads(listaSaboresBackend)

        for item in lista_sabores_backend:
            print("sabor", item["sabor"])
            print("quantidade", item["quantidade"])
            print("Preço Total:", item["precoTotalQtd"])

        comanda = Comanda(
            mesa=mesa,
            cerveja=cerveja,
            cervejaQtd=qtdCerveja,
            refrigerante=refrigerante,
            refrigeranteQtd=qtdRefrigerante,
            espetinho=espetinho,
            espetinhoQtd=qtdEspetinho,
            precoTotal=precoTotal,
            listaItensSelecionados=lista_sabores_backend,
        )

        comanda.save()
        return redirect(reverse("visualizarPedidos"))


def pedido(request, id):
    if request.method == "GET":
        comanda = get_object_or_404(Comanda, id=id)
        pedido = Comanda.objects.all()

        return render(request, "pedidoCliente.html")
