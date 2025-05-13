from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),  # Para GET
    path('usuarios/criar/', views.criar_usuario, name='criar_usuario'),  # Para POST
    path('usuarios/atualizar/<int:pk>/', views.atualizar_usuario, name='atualizar_usuario'),  # Para PUT
    path('usuarios/excluir/<int:pk>/', views.excluir_usuario, name='excluir_usuario'),  # Para DELETE
]