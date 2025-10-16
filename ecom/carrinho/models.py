from django.db import models

from produtos.models import Produto

# Create your models here.

class Carrinho(models.Model):
    car_id = models.CharField(max_length=250, blank=True)
    data_add = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.car_id
    

class ItemCarrinho(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE, null=True)
    quantidade = models.IntegerField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.produto.produto_nome