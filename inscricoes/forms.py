from django import forms
from .models import Inscricao

class InscricaoForm(forms.ModelForm):
    confirmacao = forms.BooleanField(label="Eu confirmo que as informações fornecidas estão corretas", required=True)

    class Meta:
        model = Inscricao
        fields = [
            'nome_completo',
            'nome_responsavel',
            'cpf',
            'data_nascimento',
            'email',
            'endereco',
            'cidade',
            'uf',
            'telefone',
            'irmaos',
            'unidade',
            'nivel',
            'escola',
            'selecao',
            'confirmacao'
        ]
