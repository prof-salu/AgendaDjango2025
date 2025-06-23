# agenda/urls.py

from django.urls import path
from . import views # Importe as views do seu app

app_name = 'agenda' # Define o namespace da URL para este app

urlpatterns = [
    # URL para listar todos os contatos
    path('', views.contato_lista, name='contato_lista'),
    # URL para criar um novo contato
    path('contato/novo/', views.contato_criar, name='contato_criar'),
    # URL para exibir detalhes de um contato específico
    path('contato/<int:pk>/', views.contato_detalhe, name='contato_detalhe'),
    # URL para editar um contato existente
    path('contato/<int:pk>/editar/', views.contato_editar, name='contato_editar'),
    # URL para excluir um contato
    path('contato/<int:pk>/excluir/', views.contato_excluir, name='contato_excluir'),
]