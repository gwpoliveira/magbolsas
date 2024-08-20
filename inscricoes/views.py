# views.py na app "inscricoes"

from django.shortcuts import render, redirect
from .forms import InscricaoForm

def inscricao_view(request):
    if request.method == 'POST':
        form = InscricaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inscricao_sucesso')  # Redirect para uma página de sucesso
    else:
        form = InscricaoForm()

    return render(request, 'home.html', {'form': form})  # Renderizando 'home.html'
