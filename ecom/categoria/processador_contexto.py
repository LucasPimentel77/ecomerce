from categoria.models import Categoria

def categoria_display(request):
    categorias = Categoria.objects.all()
    return {'cats': categorias}