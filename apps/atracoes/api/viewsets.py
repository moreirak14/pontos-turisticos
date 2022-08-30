from rest_framework.viewsets import ModelViewSet

from apps.atracoes.api.serializers import AtracaoSerializer
from apps.atracoes.models import Atracao


class AtracaoViewSet(ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
