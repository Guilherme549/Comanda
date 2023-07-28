from django.shortcuts import render, redirect


def visualizarPedidos(request):
    return render(request, "index.html")



def comanda(request):
    return render(request, "pedido.html")

