from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    ativo = models.BooleanField(default=False)

    def __str__(self):
        return self.nome