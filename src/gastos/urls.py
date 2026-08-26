from django.urls import path
from . import views

urlpatterns = [
    path('', views.gasto_list, name='gasto_list_api'),
    path('<int:pk>/', views.gasto_detail, name='gasto_detail_api'),
]