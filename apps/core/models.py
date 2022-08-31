from django.db import models

from apps.atracoes.models import Atracao
from apps.avaliacoes.models import Avaliacao
from apps.comentarios.models import Comentario
from apps.enderecos.models import Endereco


class DocIdentificacao(models.Model):
    descricao = models.CharField(max_length=100)


class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avaliacao)
    endereco = models.ForeignKey(
        Endereco, on_delete=models.CASCADE, null=True, blank=True
    )
    foto = models.ImageField(upload_to="pontos_turisticos", null=True, blank=True)
    doc_identificacao = models.OneToOneField(
        DocIdentificacao, on_delete=models.CASCADE, null=True, blank=True
    )

    @property
    def descricao_completa(self):
        self.aprovado = "Sim" if self.aprovado else "Não"
        return f"Nome: {self.nome} - Aprovado: {self.aprovado}"

    def __str__(self):
        return self.nome
