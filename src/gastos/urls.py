from django.urls import path
from . import views

urlpatterns = [
    path('', views.GastoListCreateView.as_view(), name='gasto_list_api'),
    path('<int:pk>/', views.GastoDetailView.as_view(), name='gasto_detail_api'),
    path('categorias/', views.CategoriaListCreateView.as_view(), name='categoria_list_api'),
    path('categorias/<int:pk>/', views.CategoriaDetailView.as_view(), name='categoria_detail_api'),
]