# agenda/forms.py

from django import forms
from .models import Contato # Importe o modelo Contato

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato # O formulário será baseado no modelo Contato
        # Campos que estarão no formulário para criação e edição
        fields = ['nome', 'telefone', 'endereco', 'email', 'data_de_nascimento']
        # Widgets para personalizar a aparência dos campos
        widgets = {
            'data_de_nascimento': forms.DateInput(attrs={'type': 'date'}),
        }