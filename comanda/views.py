from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import Comanda
import json


def visualizarPedidos(request):
    pedido = Comanda.objects.all()
    return render(request, "index.html", {"pedido": pedido})


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
        return render(request, "index.html", {"pedido": pedido})


def pedido(request):
    pedido = Comanda.objects.all()
    return render(request, "pedidoCliente.html", {"pedido": pedido})
