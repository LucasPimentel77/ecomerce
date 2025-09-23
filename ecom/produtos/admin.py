from django.contrib import admin
from .models import Produto

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('produto_nome', 'categoria', 'preco', 'estoque', 'esta_disponivel', 'criado_em', 'modificado_em')
    prepopulated_fields = {'slug': ('produto_nome',)}
    list_editable = ('preco', 'estoque', 'esta_disponivel')
    list_per_page = 20

admin.site.register(Produto, ProdutoAdmin)