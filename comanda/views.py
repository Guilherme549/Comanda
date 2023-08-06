from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Comanda
import json
from django.contrib import messages
from django.contrib.messages import constants
from decimal import Decimal


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

        if Comanda.objects.filter(mesa=mesa).exists():
            print("Mesa já está sendo usada.")
            messages.add_message(request, constants.ERROR, "Mesa ja cadastrada!")

            return redirect(reverse("comanda"))

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
    comanda = get_object_or_404(Comanda, id=id)
    if request.method == "GET":
        return render(request, "pedidoCliente.html", {"comanda": comanda})
    elif request.method == "POST":
        comanda.delete()
        return redirect(reverse("visualizarPedidos"))


def atualizarPedido(request, id):
    comanda = get_object_or_404(Comanda, id=id)
    if request.method == "GET":
        return render(request, "atualizarPedido.html", {"comanda": comanda})
    elif request.method == "POST":
        cerveja = request.POST.get("cerveja")
        qtdCerveja = int(request.POST.get("qtdCerveja"))
        refrigerante = request.POST.get("refrigerantes")
        qtdRefrigerante = int(request.POST.get("qtdRefrigerante"))
        espetinho = request.POST.get("espetinhos")
        qtdEspetinho = int(request.POST.get("qtdEspetinho"))
        precoTotal = request.POST.get("precoTotal")

        listaSaboresBackend = request.POST.get("listaSaboresBackend")
        lista_sabores_backend = json.loads(listaSaboresBackend)

        # Atualiza os dados do objeto com os novos valores
        comanda.cerveja = cerveja
        comanda.cervejaQtd = qtdCerveja
        comanda.refrigerante = refrigerante
        comanda.refrigeranteQtd = qtdRefrigerante
        comanda.espetinho = espetinho
        comanda.espetinhoQtd = qtdEspetinho
        precoTotal_decimal = Decimal(precoTotal)
        comanda.precoTotal += precoTotal_decimal
        comanda.listaItensSelecionados += lista_sabores_backend

        # Salva as alterações no banco de dados
        comanda.save()

        return render(request, "pedidoCliente.html", {"comanda": comanda})


def pesquisarMesa(request):
    if request.method == "GET":
        mesa = request.GET.get("mesa")
        if mesa:
            pedidos = Comanda.objects.filter(mesa__icontains=mesa)
        else:
            pedidos = Comanda.objects.all()

        return render(request, "index.html", {"pedidos": pedidos})
    else:
        return redirect(reverse("visualizarPedidos"))
