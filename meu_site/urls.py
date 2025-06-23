# meu_site/urls.py

from django.contrib import admin
from django.urls import path, include # Importe 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agenda/', include('agenda.urls')), # Inclua as URLs do seu app 'agenda'
]

