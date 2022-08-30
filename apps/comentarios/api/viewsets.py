from rest_framework.viewsets import ModelViewSet
from apps.comentarios.models import Comentario
from apps.comentarios.api.serializers import ComentarioSerializer


class ComentarioViewSet(ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
