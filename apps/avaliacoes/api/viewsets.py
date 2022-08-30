from rest_framework.viewsets import ModelViewSet
from apps.avaliacoes.models import Avaliacao
from apps.avaliacoes.api.serializers import AvalicaoSerializer


class AvaliacaoViewSet(ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvalicaoSerializer
