# Generated by Django 2.2.6 on 2020-02-12 00:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('correcao', '0006_auto_20200211_2106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='redacao',
            name='teste',
        ),
    ]
