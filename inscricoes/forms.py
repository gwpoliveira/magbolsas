from django import forms
from .models import Inscricao
from captcha.fields import CaptchaField

class InscricaoForm(forms.ModelForm):
    confirmacao = forms.BooleanField(label="Eu confirmo que as informações fornecidas estão corretas", required=True)
    captcha = CaptchaField(label='Por favor, verifique que você não é um robô')

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
            'confirmacao',
            'captcha'
        ]
