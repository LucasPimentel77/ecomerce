from django.shortcuts import get_object_or_404, render
from categoria.models import Categoria
from produtos.models import Produto

def visualizarProdutos(request, slug=None):
    categoria = None
    produtos = None

    if slug != None:
        categoria = get_object_or_404(Categoria, slug=slug)
        produtos = Produto.objects.filter(categoria=categoria, esta_disponivel=True)
        produtos_quant = produtos.count()
    
    else:
        produtos = Produto.objects.all().filter(esta_disponivel=True).order_by('criado_em')
        produtos_quant = produtos.count()

    contexto = {
        'produtos': produtos,
        'produtos_quant': produtos_quant,
    }
    return render(request, 'produtos/produtos.html', contexto)