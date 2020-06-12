from django.contrib import admin
from .models import Curso, Turma, Aluno

from correcao.form import TextoForm

from redacoes.models import Tema
from correcao.models import Texto

# Register your models here.

admin.site.register (Curso)
admin.site.register (Turma)
admin.site.register (Aluno)
admin.site.register (Tema)
admin.site.register (Texto)

