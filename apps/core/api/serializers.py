from rest_framework import serializers

from apps.atracoes.api.serializers import AtracaoSerializer
from apps.avaliacoes.api.serializers import AvalicaoSerializer
from apps.comentarios.api.serializers import ComentarioSerializer
from apps.core.models import DocIdentificacao, PontoTuristico
from apps.enderecos.api.serializers import EnderecoSerializer


class DocIdentificacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocIdentificacao
        fields = "__all__"


class PontoTuristicoSerializer(serializers.ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    comentarios = ComentarioSerializer(many=True)
    avaliacoes = AvalicaoSerializer(many=True)
    endereco = EnderecoSerializer()
    doc_identificacao = DocIdentificacaoSerializer()

    class Meta:
        model = PontoTuristico
        fields = [
            "id",
            "nome",
            "descricao",
            "aprovado",
            "atracoes",
            "comentarios",
            "avaliacoes",
            "endereco",
            "foto",
            "descricao_completa",
            "doc_identificacao",
        ]
