# Generated by Django 2.2.6 on 2020-02-05 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redacoes', '0003_auto_20200205_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tema',
            name='arquivo',
            field=models.FileField(upload_to='', verbose_name='Textos motivadores'),
        ),
    ]