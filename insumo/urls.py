from django.urls import path
from . import views 

urlpatterns = [
    path("", views.insumo, name="insumo_page"),
    path("crear_insumo/", views.crear_insumo, name='crear_insumo_page'),
]
