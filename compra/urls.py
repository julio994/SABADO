from django.urls import path
from . import views 

urlpatterns = [
        path('', views.listar_compras, name='compra-list'),
        path('nueva/', views.crear_compra, name='compra-create'),
         path('compra/<int:compra_id>/', views.detalle_compra, name='detalle_compra'),
       
]