from django.urls import path
from . import views 

urlpatterns = [
    path("", views.medida, name="medida_page"),
    path("crear_medida/", views.crear_medida, name='crear_medida_page'),
]
