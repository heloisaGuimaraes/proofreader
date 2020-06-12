from django.db import models
from usuarios.models import Aluno, Turma
from redacoes.models import Tema


# Create your models here.

class Texto (models.Model):
    aluno = models.ForeignKey (Aluno, on_delete=models.CASCADE )
    
    Tema_da_redacao = models.ForeignKey (Tema, on_delete=models.CASCADE, verbose_name ='Tema')

    texto = models.FileField(verbose_name="Texto dissertativo argumentativo", upload_to="", help_text = "Adicione um arquivo em formato PDF contendo o texto do aluno")
   
    situacoes_choices = [('-', '-----'),('branco', 'Branco'), ('insuficiente', 'Insuficiente'), ('nulo', 'Nulo'), ('fuga_ao_tema', 'Fuga ao Tema'), ('parte_desconectada', 'Parte Desconectada')]

    situacao = models.CharField( verbose_name ='Situação',max_length = 20, choices = situacoes_choices, default = '-----')

    c_1 = models.IntegerField(verbose_name='Competência 1',default=0)
    c_2 = models.IntegerField(verbose_name='Competência 2',default=0)
    c_3 = models.IntegerField(verbose_name='Competência 3',default=0)
    c_4 = models.IntegerField(verbose_name='Competência 4',default=0)
    c_5 = models.IntegerField(verbose_name='Competência 5',default=0)

    class META:
        verbose_name = "Redação"
        verbose_name_plural = "Redações"

    #def chage_view (self):
        #return self.Nome_do_aluno 
    #def __str__(self):
        #return self.aluno
    


