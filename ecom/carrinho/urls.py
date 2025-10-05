from django.urls import path, include

from carrinho import views


urlpatterns = [
    path('', views.visualizarCarrinho, name='carrinho'),
    path('adicionar/<int:produto_id>/', views.adicionarAoCarrinho, name='adicionar_ao_carrinho'),
]
