# Generated by Django 2.2.6 on 2020-01-30 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_turma'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alunos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=100)),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Turma')),
            ],
        ),
    ]
