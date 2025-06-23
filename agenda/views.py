# agenda/views.py

from django.shortcuts import render, redirect, get_object_or_404 # Importe 'redirect'
from .models import Contato # Importe o seu modelo Contato
from .forms import ContatoForm # Importe o seu formulário ContatoForm

def contato_lista(request):
    # Obtém todos os contatos do banco de dados, ordenados por nome
    contatos = Contato.objects.all().order_by('nome')
    # Renderiza o template 'contato_lista.html', passando os contatos como contexto
    return render(request, 'agenda/contato_lista.html', {'contatos': contatos})

def contato_criar(request):
    if request.method == 'POST':
        # Se a requisição for POST, o formulário foi enviado
        form = ContatoForm(request.POST) # Preenche o formulário com os dados enviados
        if form.is_valid():
            # Se o formulário for válido, salva o novo contato no banco de dados
            form.save()
            return redirect('agenda:contato_lista') # Redireciona para a lista de contatos
    else:
        # Se a requisição for GET, exibe um formulário vazio
        form = ContatoForm()
    # Renderiza o template, passando o formulário como contexto e um título para a página
    return render(request, 'agenda/contato_form.html', {'form': form, 'titulo_pagina': 'Adicionar Contato'})

def contato_detalhe(request, pk):
    # Tenta obter o contato pelo ID (pk), ou levanta um erro 404 se não encontrado
    contato = get_object_or_404(Contato, pk=pk)
    # Renderiza o template 'contato_detalhe.html', passando o contato como contexto
    return render(request, 'agenda/contato_detalhe.html', {'contato': contato})