from django.db import models

# Create your models here.

class Tema (models.Model):
    tema = models.CharField(max_length=150)
    arquivo = models.FileField(verbose_name="Textos motivadores", upload_to="", help_text = "Adicione um arquivo em formato PDF contendo todos os textos motivadores")
    def chage_view (self):
        return self.arquivo 
    observacoes = models.TextField(verbose_name = "Observações", null=True, blank=True)

    
    def __str__(self):
        return self.tema