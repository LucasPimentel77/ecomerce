from django.contrib import admin

from carrinho.models import Carrinho, ItemCarrinho

# Register your models here.
class CarrinhoAdmin(admin.ModelAdmin):
    list_display = ('car_id', 'data_add')
    search_fields = ('car_id',)

class ItemCarrinhoAdmin(admin.ModelAdmin):
    list_display = ('produto', 'carrinho', 'quantidade', 'ativo')
    search_fields = ('produto__produto_nome', 'carrinho__car_id')

admin.site.register(Carrinho, CarrinhoAdmin)
admin.site.register(ItemCarrinho, ItemCarrinhoAdmin)