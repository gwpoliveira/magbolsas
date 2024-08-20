# admin.py na app "inscricoes"
from django.contrib import admin
from .models import Inscricao

@admin.register(Inscricao)
class InscricaoAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'nome_responsavel', 'email', 'telefone', 'unidade', 'nivel')
    search_fields = ('nome_completo', 'email', 'telefone')
    list_filter = ('unidade', 'nivel')


