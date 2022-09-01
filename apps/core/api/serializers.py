from rest_framework import serializers

from apps.atracoes.api.serializers import AtracaoSerializer
from apps.atracoes.models import Atracao
from apps.avaliacoes.api.serializers import AvalicaoSerializer
from apps.avaliacoes.models import Avaliacao
from apps.comentarios.api.serializers import ComentarioSerializer
from apps.comentarios.models import Comentario
from apps.core.models import DocIdentificacao, PontoTuristico
from apps.enderecos.api.serializers import EnderecoSerializer
from apps.enderecos.models import Endereco


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

    def _cria_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            atr = Atracao.objects.create(**atracao)
            ponto.atracoes.add(atr)

    def _cria_avaliacoes(self, avaliacoes, ponto):
        for avaliacao in avaliacoes:
            ava = Avaliacao.objects.create(**avaliacao)
            ponto.avaliacoes.add(ava)

    def _cria_comentarios(self, comentarios, ponto):
        for comentario in comentarios:
            comen = Comentario.objects.create(**comentario)
            ponto.comentarios.add(comen)

    def create(self, validated_data):
        atracoes = validated_data["atracoes"]
        del validated_data["atracoes"]

        avaliacoes = validated_data["avaliacoes"]
        del validated_data["avaliacoes"]

        comentarios = validated_data["comentarios"]
        del validated_data["comentarios"]

        endereco = validated_data["endereco"]
        del validated_data["endereco"]

        doc_identificacao = validated_data["doc_identificacao"]
        del validated_data["doc_identificacao"]

        ponto = PontoTuristico.objects.create(**validated_data)

        self._cria_atracoes(atracoes=atracoes, ponto=ponto)

        self._cria_avaliacoes(avaliacoes=avaliacoes, ponto=ponto)

        self._cria_comentarios(comentarios=comentarios, ponto=ponto)

        end = Endereco.objects.create(**endereco)
        ponto.endereco = end

        doc_in = DocIdentificacao.objects.create(**doc_identificacao)
        ponto.doc_identificacao = doc_in

        ponto.save()

        return ponto
