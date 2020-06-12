from django.db import models

# Create your models here.

class Curso (models.Model):
    nome_do_curso = models.CharField (max_length=30)

    def __str__(self):
        return self.nome_do_curso

class Turma (models.Model):
    nome_da_turma = models.CharField(max_length=30)
    ano = models.IntegerField(help_text = "Entre com o ano em que a turma está ativa. Ex.: 2020")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    observacoes = models.TextField(verbose_name = "Observações", null=True, blank=True)

    def __str__(self):
        return self.nome_da_turma

class Aluno (models.Model):
    turma = models.ForeignKey (Turma, on_delete=models.CASCADE)
    nome_completo = models.CharField (max_length= 100)

    def __str__(self):
        return self.nome_completo