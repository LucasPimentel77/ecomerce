from django.http import HttpResponse
from django.shortcuts import render
from produtos.models import Produto



def visualizarHome(request):
    produtos = Produto.objects.all().filter(esta_disponivel=True).order_by('criado_em')[:8]
    
    contexto = {
        'produtos': produtos,
    }

    return render(request, 'home.html', contexto)
