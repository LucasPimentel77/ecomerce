from django.urls import path
from produtos import views

urlpatterns = [
    path('', views.visualizarProdutos, name='produtos'),
    path('<slug:categoria_slug>/', views.visualizarProdutos, name='produtos_por_categoria'),
    path('<slug:categoria_slug>/<slug:produto_slug>/', views.produtoDetalhe, name='produto_detalhe'),
]