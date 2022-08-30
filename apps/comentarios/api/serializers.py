from rest_framework import serializers

from apps.comentarios.models import Comentario


class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ["id", "usuario", "comentario", "data", "aprovado"]
