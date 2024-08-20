# models.py na app "inscricoes"
from django.db import models

class Inscricao(models.Model):
    nome_completo = models.CharField(verbose_name='Nome Completo do Candidato:', max_length=255)
    nome_responsavel = models.CharField(verbose_name='Nome do Resposavel:', max_length=255)
    email = models.EmailField()
    telefone = models.CharField(verbose_name='Telefone para contado:', max_length=15)
    endereco = models.TextField(verbose_name='Endereço:', blank=True)
    irmaos = models.CharField(verbose_name='Tem irmãos?', max_length=20, choices=[('Não', 'Não Tenho'),('Um', 'Um'), ('Dois', 'Dois'), ('Três ou Mais', 'Três ou Mais')])
    unidade = models.CharField(max_length=50, choices=[('Primavera', 'Unidade Primavera'), ('Bela Vista', 'Unidade Bela Vista')])
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
    motivo_bolsa = models.TextField()

    def __str__(self):
        return self.nome_completo