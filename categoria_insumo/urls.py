from django.urls import path
from . import views 

urlpatterns = [
    path("", views.categoria_insumo, name="categoriai_page"),
    path("crear_categoria/", views.crear_categoria, name='crear_categoria_page'),
]
