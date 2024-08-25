from django.contrib import admin
from .models import Inscricao
import openpyxl
from django.http import HttpResponse

@admin.action(description='Exportar para Excel')
def exportar_excel(modeladmin, request, queryset):
    # Cria uma nova planilha Excel
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Inscrições"

    # Escreve o cabeçalho
    headers = ['Nome Completo', 'Nome do Responsável', 'CPF', 'Data de Nascimento', 'Email', 'Endereço',
               'Cidade', 'UF', 'Telefone', 'Irmãos', 'Unidade', 'Nível', 'Escola', 'Como soube', 'Confirmação']
    ws.append(headers)

    # Escreve os dados das inscrições selecionadas
    for inscricao in queryset:
        ws.append([
            inscricao.nome_completo,
            inscricao.nome_responsavel,
            inscricao.cpf,
            inscricao.data_nascimento,
            inscricao.email,
            inscricao.endereco,
            inscricao.cidade,
            inscricao.uf,
            inscricao.telefone,
            inscricao.irmaos,
            inscricao.unidade,
            inscricao.nivel,
            inscricao.escola,
            inscricao.selecao,
            inscricao.confirmacao
        ])

    # Cria a resposta HTTP com o arquivo Excel
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=inscricoes.xlsx'
    wb.save(response)
    return response

@admin.register(Inscricao)
class InscricaoAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'nome_responsavel', 'email', 'telefone', 'unidade', 'nivel')
    search_fields = ('nome_completo', 'email', 'telefone')
    list_filter = ('unidade', 'nivel')
    actions = [exportar_excel]  # Adiciona a ação personalizada
