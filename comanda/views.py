from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Comanda
from decimal import Decimal


def visualizarPedidos(request):
    return render(request, "index.html")


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

        listaSabores = request.POST.get("listaSabores")
        if precoTotal:
            precoTotal = Decimal(precoTotal)
        else:
            precoTotal = Decimal('0.00')

        print(listaSabores)

        comanda = Comanda(
            mesa=mesa,
            cerveja=cerveja,
            cervejaQtd=qtdCerveja,
            refrigerante=refrigerante,
            refrigeranteQtd=qtdRefrigerante,
            espetinho=espetinho,
            espetinhoQtd=qtdEspetinho,
            precoTotal=precoTotal,
        )

        comanda.save()
        pedido = Comanda.objects.all()
        return render(request, "index.html", {"pedido": pedido})