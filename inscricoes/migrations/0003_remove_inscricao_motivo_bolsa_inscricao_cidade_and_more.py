# Generated by Django 5.1 on 2024-08-22 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscricoes', '0002_alter_inscricao_endereco_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inscricao',
            name='motivo_bolsa',
        ),
        migrations.AddField(
            model_name='inscricao',
            name='cidade',
            field=models.CharField(blank=True, max_length=255, verbose_name='Cidade:'),
        ),
        migrations.AddField(
            model_name='inscricao',
            name='confirmacao',
            field=models.BooleanField(default=False, verbose_name='Eu confirmo que as informações fornecidas estão corretas'),
        ),
        migrations.AddField(
            model_name='inscricao',
            name='cpf',
            field=models.CharField(default='00000000000', max_length=11, unique=True, verbose_name='CPF'),
        ),
        migrations.AddField(
            model_name='inscricao',
            name='data_nascimento',
            field=models.DateField(blank=True, null=True, verbose_name='Data de Nascimento'),
        ),
        migrations.AddField(
            model_name='inscricao',
            name='escola',
            field=models.CharField(default='Escola Padrão', max_length=255, verbose_name='Escola que já estudou'),
        ),
        migrations.AddField(
            model_name='inscricao',
            name='selecao',
            field=models.CharField(choices=[('Instagram', 'Instagram'), ('Facebook', 'Facebook'), ('Twitter', 'Twitter'), ('YouTube', 'YouTube'), ('Grupos Whatsapp', 'Grupos Whatsapp'), ('Coordenação / Professores', 'Coordenação / Professores'), ('Pais', 'Pais'), ('Alunos', 'Alunos')], default='Não informado', max_length=50),
        ),
        migrations.AddField(
            model_name='inscricao',
            name='uf',
            field=models.CharField(blank=True, max_length=2, verbose_name='UF:'),
        ),
        migrations.AlterField(
            model_name='inscricao',
            name='endereco',
            field=models.CharField(blank=True, max_length=255, verbose_name='Endereço:'),
        ),
        migrations.AlterField(
            model_name='inscricao',
            name='nome_completo',
            field=models.CharField(blank=True, max_length=255, verbose_name='Nome Completo do Candidato:'),
        ),
        migrations.AlterField(
            model_name='inscricao',
            name='nome_responsavel',
            field=models.CharField(blank=True, max_length=255, verbose_name='Nome do Responsável:'),
        ),
        migrations.AlterField(
            model_name='inscricao',
            name='telefone',
            field=models.CharField(blank=True, max_length=15, verbose_name='Telefone para contado:'),
        ),
        migrations.AlterField(
            model_name='inscricao',
            name='unidade',
            field=models.CharField(blank=True, choices=[('Primavera', 'Unidade Primavera'), ('Bela Vista', 'Unidade Bela Vista')], max_length=50),
        ),
    ]
