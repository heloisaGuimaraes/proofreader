# Generated by Django 2.2.6 on 2020-02-12 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('correcao', '0008_redacao_teste'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redacao',
            name='teste',
            field=models.CharField(choices=[('branco', 'Branco'), ('insuficiente', 'Insuficiente'), ('nulo', 'Nulo'), ('fuga_ao_tema', 'Fuga ao Tema'), ('parte_desconectada', 'Parte Desconectada')], default='-----', max_length=20),
        ),
    ]