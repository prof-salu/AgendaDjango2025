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

def contato_editar(request, pk):
    # Obtém o contato existente pelo ID (pk), ou levanta 404 se não encontrado
    contato = get_object_or_404(Contato, pk=pk)
    if request.method == 'POST':
        # Se a requisição for POST, o formulário foi enviado com novos dados
        # 'instance=contato' é crucial: informa ao formulário que ele deve ATUALIZAR este objeto
        form = ContatoForm(request.POST, instance=contato)
        if form.is_valid():
            # Se o formulário for válido, salva (atualiza) o contato no banco de dados
            form.save()
            # Redireciona para a página de detalhes do contato atualizado
            return redirect('agenda:contato_detalhe', pk=contato.pk)
    else:
        # Se a requisição for GET, exibe o formulário preenchido com os dados atuais do contato
        form = ContatoForm(instance=contato)
    # Renderiza o template, passando o formulário, o contato e um título para a página
    return render(request, 'agenda/contato_form.html', {'form': form, 'contato': contato, 'titulo_pagina': 'Editar Contato'})

def contato_excluir(request, pk):
    contato = get_object_or_404(Contato, pk=pk)
    if request.method == 'POST':
        # Se a requisição for POST, significa que o usuário confirmou a exclusão
        contato.delete() # Exclui o contato do banco de dados
        return redirect('agenda:contato_lista') # Redireciona para a lista
    # Se a requisição for GET, exibe a página de confirmação
    return render(request, 'agenda/contato_confirm_delete.html', {'contato': contato})
    return render(request, 'agenda/contato_confirm_delete.html', {'contato': contato})