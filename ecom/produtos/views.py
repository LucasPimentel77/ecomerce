from django.shortcuts import get_object_or_404, render
from categoria.models import Categoria
from produtos.models import Produto

def visualizarProdutos(request, categoria_slug=None):
    categoria = None
    produtos = None

    if categoria_slug != None:
        categoria = get_object_or_404(Categoria, slug=categoria_slug)
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

def produtoDetalhe(request, categoria_slug, produto_slug):
    try:
        produto = Produto.objects.get(categoria__slug=categoria_slug, slug=produto_slug)
    except Exception as e:
        raise e

    contexto = {
        'produto': produto,
    }
    return render(request, 'produtos/produto_detalhe.html', contexto)