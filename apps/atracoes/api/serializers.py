from rest_framework import serializers
from apps.atracoes.models import Atracao


class AtracaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atracao
        fields = [
            "id",
            "nome",
            "descricao",
            "horario_func",
            "idade_minima",
            "observacoes",
        ]
