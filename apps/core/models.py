from django.db import models

from apps.atracoes.models import Atracao
from apps.comentarios.models import Comentario


class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentario)

    def __str__(self):
        return self.nome
