from django.shortcuts import redirect, render

from carrinho.models import Carrinho, ItemCarrinho
from produtos.models import Produto

# Create your views here.

def _getCarrinhoId(request):
    carrinho_id = request.session.session_key
    if not carrinho_id:
        carrinho_id = request.session.create()
    return carrinho_id

def visualizarCarrinho(request, total=0, quantidade=0, item_carrinho=None):
    try:
        carrinho = Carrinho.objects.get(car_id=_getCarrinhoId(request))
        item_carrinho = ItemCarrinho.objects.filter(carrinho=carrinho, ativo=True)
        for item in item_carrinho:
            total += (item.produto.preco * item.quantidade)
            quantidade += item.quantidade
    except Carrinho.DoesNotExist:
        pass
    context = {
        'total': total,
        'quantidade': quantidade,
        'item_carrinho': item_carrinho,
    }

    return render(request, 'produtos/carrinho.html', context)

def adicionarAoCarrinho(request, produto_id):
    # obter o produto
    produto = Produto.objects.get(id=produto_id)

    # obter ou criar o carinho
    try:
        carrinho = Carrinho.objects.get(car_id=_getCarrinhoId(request))
        carrinho.save()
    except Carrinho.DoesNotExist:
        carrinho = Carrinho.objects.create(
            car_id=_getCarrinhoId(request)
        )
        carrinho.save()

    # criar o item do carrinho
    try:
        item_carrinho = ItemCarrinho.objects.get(produto=produto, carrinho=carrinho)
        item_carrinho.quantidade += 1
        item_carrinho.save()
    except ItemCarrinho.DoesNotExist:
        item_carrinho = ItemCarrinho.objects.create(
            produto=produto,
            quantidade=1,
            carrinho=carrinho
        )
        item_carrinho.save()

    return redirect('carrinho')    
