from .models import Carrinho, ItemCarrinho
from .views import _getCarrinhoId


def contador(request){
    car_cont = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            car = Carrinho.objects.filter(car=_getCarId(request))
            car_items = ItemCarrinho.objects.all().filter(car = car[:1])

            for car_item in car_items:
                car_cont += car_item.quantidade
        except Carrinho.DoesNotExist:
            car_cont = 0

        return {"contador": car_cont}
}