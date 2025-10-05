from django.db import models
from django.urls import reverse

class Produto(models.Model):
    categoria = models.ForeignKey('categoria.Categoria', on_delete=models.CASCADE)
    produto_nome = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    descricao = models.TextField(max_length=300, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='fotos/produtos/', blank=True)
    estoque = models.IntegerField()
    esta_disponivel = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now=True)
    modificado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.produto_nome
    
    def get_url(self):
        return reverse('produto_detalhe', args=[self.categoria.slug, self.slug])
