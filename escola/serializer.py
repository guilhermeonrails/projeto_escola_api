from rest_framework import serializers
from escola.models import Aluno

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['nome', 'rg', 'cpf', 'data_nascimento', 'ativo']