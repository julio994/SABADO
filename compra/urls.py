from django.urls import path
from . import views 

urlpatterns = [
        path('', views.listar_compras, name='compra-list'),
        path('nueva/', views.crear_compra_y_detalles, name='compra-create'),
       
]