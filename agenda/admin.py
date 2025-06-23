from django.contrib import admin
from .models import Contato # Importe o seu modelo Contato

# Registre o seu modelo aqui para que ele apareça no Django Admin
admin.site.register(Contato)