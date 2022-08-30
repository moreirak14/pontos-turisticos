from rest_framework import serializers

from apps.core.models import PontoTuristico


class PontoTuristicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PontoTuristico
        fields = ["id", "nome", "descricao"]
