# Generated by Django 3.0.4 on 2020-03-31 01:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('correcao', '0014_auto_20200331_0113'),
    ]

    operations = [
        migrations.RenameField(
            model_name='texto',
            old_name='Nome_do_aluno',
            new_name='aluno',
        ),
    ]
