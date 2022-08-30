from rest_framework.viewsets import ModelViewSet

from apps.comentarios.api.serializers import ComentarioSerializer
from apps.comentarios.models import Comentario


class ComentarioViewSet(ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
