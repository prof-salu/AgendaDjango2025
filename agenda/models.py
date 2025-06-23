from django.db import models

# Cria o modelo para os contatos da agenda
class Contato(models.Model):
    # Campo para o nome do contato, obrigatório
    nome = models.CharField(max_length=255)
    # Campo para o telefone, pode ser vazio
    telefone = models.CharField(max_length=20, blank=True, null=True)
    # Campo para o endereço, pode ser vazio
    endereco = models.TextField(blank=True, null=True)
    # Campo para o e-mail, pode ser vazio e é validado como e-mail
    email = models.EmailField(blank=True, null=True)
    # Campo para a data de nascimento, pode ser vazio
    data_de_nascimento = models.DateField(blank=True, null=True)
    # Campo para a data de criação do contato (preenchido automaticamente)
    created_at = models.DateTimeField(auto_now_add=True)

    # Método para representar o objeto Contact como uma string legível
    def __str__(self):
        return f'{self.nome} [{self.email}]'