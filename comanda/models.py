from django.db import models
from django.utils import timezone


class Comanda(models.Model):
    mesa = models.IntegerField()
    cerveja = models.CharField(max_length=20, null=True)
    refrigerante = models.CharField(max_length=20, null=True)
    espetinho = models.CharField(max_length=20, null=True)

    # Qtd
    cervejaQtd = models.IntegerField(null=True)
    refrigeranteQtd = models.IntegerField(null=True)
    espetinhoQtd = models.IntegerField(null=True)

    # preco
    cervejaPrecoTotal = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    refrigerantePrecoTotal = models.DecimalField(
        max_digits=10, decimal_places=2, null=True
    )
    espetinhoPrecoTotal = models.DecimalField(
        max_digits=10, decimal_places=2, null=True
    )
    precoTotal = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    # arquivo json
    listaItensSelecionados = models.JSONField(null=True)

    data = models.DateField(null=True, blank=True, auto_now_add=True)
    horario = models.TimeField(null=True, blank=True, auto_now_add=True)
    def __str__(self):
        return str(self.mesa)
