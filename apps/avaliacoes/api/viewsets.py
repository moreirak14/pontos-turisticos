from rest_framework.viewsets import ModelViewSet

from apps.avaliacoes.api.serializers import AvalicaoSerializer
from apps.avaliacoes.models import Avaliacao


class AvaliacaoViewSet(ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvalicaoSerializer
