# Generated by Django 2.2.6 on 2020-02-11 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('correcao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='redacao',
            name='teste',
            field=models.BooleanField(null=True),
        ),
    ]