from django.urls import path
from produtos import views

urlpatterns = [
    path('', views.visualizarProdutos, name='produtos'),
    path('<slug:slug>/', views.visualizarProdutos, name='produtos_por_categoria'),
]