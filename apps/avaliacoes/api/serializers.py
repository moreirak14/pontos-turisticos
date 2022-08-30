from rest_framework import serializers

from apps.avaliacoes.models import Avaliacao


class AvalicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ["id", "usuario", "comentario", "nota", "data"]
