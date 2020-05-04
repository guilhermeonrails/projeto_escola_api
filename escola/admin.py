from django.contrib import admin
from escola.models import Aluno

class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento', 'ativo')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ('ativo',)
    list_editable = ('ativo',)
    list_per_page = 10

admin.site.register(Aluno, Alunos)