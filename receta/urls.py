from django.urls import path
from . import views

urlpatterns = [
    path('', views.receta_list, name='receta_list'),
    path('crear/', views.receta_create, name='receta_create'),
    path('<int:id>/', views.receta_detail, name='receta_detail'),
    path('editar/<int:pk>/', views.receta_update, name='receta_update'),
]