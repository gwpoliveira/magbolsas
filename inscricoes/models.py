from django.db import models

class Inscricao(models.Model):
    nome_completo = models.CharField(verbose_name='Nome Completo do Candidato:', max_length=255, blank=True)
    nome_responsavel = models.CharField(verbose_name='Nome do Responsável:', max_length=255, blank=True)
    cpf = models.CharField(verbose_name='CPF', max_length=11, unique=True, default='00000000000')
    data_nascimento = models.DateField(verbose_name='Data de Nascimento', blank=True, null=True)  # null=True adicionado
    email = models.EmailField()
    endereco = models.CharField(verbose_name='Endereço:', max_length=255, blank=True)  # max_length adicionado
    cidade = models.CharField(verbose_name='Cidade:', max_length=255, blank=True)  # max_length adicionado
    uf = models.CharField(verbose_name='UF:', max_length=2, blank=True)  # max_length adicionado e alterado para CharField
    telefone = models.CharField(verbose_name='Telefone para contado:', max_length=15, blank=True)
    irmaos = models.CharField(verbose_name='Tem irmãos?', max_length=20, choices=[('Não', 'Não Tenho'),('Um', 'Um'), ('Dois', 'Dois'), ('Três ou Mais', 'Três ou Mais')])
    unidade = models.CharField(max_length=50, choices=[('Primavera', 'Unidade Primavera'), ('Bela Vista', 'Unidade Bela Vista')], blank=True)
    nivel = models.CharField(max_length=50, choices=[
        ('Maternal Babay', 'Maternal Babay'),
        ('1º ano Fundamental I', '1º ano Fundamental I'),
        ('2º ano Fundamental I', '2º ano Fundamental I'),
        ('3º ano Fundamental I', '3º ano Fundamental I'),
        ('4º ano Fundamental I', '4º ano Fundamental I'),
        ('5º ano Fundamental II', '5º ano Fundamental II'),
        ('6º ano Fundamental II', '6º ano Fundamental II'),
        ('7º ano Fundamental II', '7º ano Fundamental II'),
        ('8º ano Fundamental II', '8º ano Fundamental II'),
        ('9º ano Fundamental II', '9º ano Fundamental II'),
        ('1ª Série do Ensino Médio', '1ª Série do Ensino Médio'),
        ('2ª Série do Ensino Médio', '2ª Série do Ensino Médio'),
        ('3ª Série do Ensino Médio', '3ª Série do Ensino Médio')
    ])
    escola = models.CharField(verbose_name='Escola que já estudou', max_length=255, default='Escola Padrão')
    selecao = models.CharField(max_length=50, choices=[
        ('Instagram', 'Instagram'),
        ('Facebook', 'Facebook'),
        ('Twitter', 'Twitter'),
        ('YouTube', 'YouTube'),
        ('Grupos Whatsapp', 'Grupos Whatsapp'),
        ('Coordenação / Professores', 'Coordenação / Professores'),
        ('Pais', 'Pais'),
        ('Alunos', 'Alunos')
    ], default='Não informado')

    confirmacao = models.BooleanField(verbose_name='Eu confirmo que as informações fornecidas estão corretas', default=False)

    def __str__(self):
        return self.nome_completo
