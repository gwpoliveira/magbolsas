# views.py na app "inscricoes"
import openpyxl
from django.shortcuts import render, redirect
from .forms import InscricaoForm
from django.http import HttpResponse
from .models import Inscricao
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def inscricao_view(request):
    if request.method == 'POST':
        form = InscricaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inscricao_sucesso')  # Redirect para uma página de sucesso
    else:
        form = InscricaoForm()

    return render(request, 'home.html', {'form': form})  # Renderizando 'home.html'

def inscricao_sucesso(request):
    return render(request, 'inscricao_sucesso.html')

def download_excel(request):
    # Criar um workbook e uma sheet
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Inscrições"

    # Cabeçalhos da planilha
    ws.append([
        "Nome Completo", "Nome do Responsável", "CPF",
        "Data de Nascimento", "Email", "Endereço",
        "Cidade", "UF", "Telefone", "Irmãos",
        "Unidade", "Nível", "Escola", "Como soube do processo"
    ])

    # Inserir dados das inscrições na planilha
    inscricoes = Inscricao.objects.all()
    for inscricao in inscricoes:
        ws.append([
            inscricao.nome_completo, inscricao.nome_responsavel, inscricao.cpf,
            inscricao.data_nascimento, inscricao.email, inscricao.endereco,
            inscricao.cidade, inscricao.uf, inscricao.telefone, inscricao.irmaos,
            inscricao.unidade, inscricao.nivel, inscricao.escola, inscricao.selecao
        ])

    # Preparar a resposta HTTP para download do arquivo Excel
    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response['Content-Disposition'] = 'attachment; filename=inscricoes.xlsx'

    wb.save(response)
    return response

@login_required
def lista_inscritos(request):
    search_query = request.GET.get('search', '')
    if search_query:
        inscritos = Inscricao.objects.filter(nome_completo__icontains=search_query)
    else:
        inscritos = Inscricao.objects.all()

    paginator = Paginator(inscritos, 50)  # Mostra 50 inscritos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'lista_inscritos.html', {'page_obj': page_obj, 'search_query': search_query})