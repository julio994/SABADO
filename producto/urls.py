from django.urls import path
from . import views 

urlpatterns = [
    path("", views.producto, name="producto_list"),
    path("crear_producto/", views.crear_producto, name='crear_producto'),
]
