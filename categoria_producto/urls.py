from django.urls import path
from . import views 

urlpatterns = [
    path("", views.categoria_producto, name="categoriap_list"),
    path("crear_categoria_producto/", views.crear_categoria_producto, name='crear_categoria_producto'),
]
