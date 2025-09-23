from django.shortcuts import render
from produtos.models import Produto

def visualizarProdutos(request):
    return render(request, 'produtos/produtos.html')

def visualizarHome(request):
    produtos = Produto.objects.all().filter(esta_disponivel=True).order_by('criado_em')[:8]
    
    contexto = {
        'produtos': produtos,
    }

    return render(request, 'home.html', contexto)
