# forms.py na app "inscricoes"

from django import forms
from .models import Inscricao

class InscricaoForm(forms.ModelForm):
    class Meta:
        model = Inscricao
        fields = [
            'nome_completo',
            'nome_responsavel',
            'email',
            'telefone',
            'endereco',
            'irmaos',
            'unidade',
            'nivel',
            'motivo_bolsa'
        ]
