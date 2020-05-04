from rest_framework import viewsets
from escola.models import Aluno
from escola.serializer import AlunoSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    """Alunos ativos"""
    queryset = Aluno.objects.all().filter(ativo=True)
    serializer_class = AlunoSerializer

class TodosAlunosViewSet(viewsets.ModelViewSet):
    """Alunos ativos e inativos"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer