# Generated by Django 5.1 on 2024-09-19 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscricoes', '0007_alter_inscricao_confirmacao_alter_inscricao_irmaos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscricao',
            name='unidade',
            field=models.CharField(blank=True, choices=[('Primavera', 'Unidade Primavera')], max_length=50),
        ),
    ]