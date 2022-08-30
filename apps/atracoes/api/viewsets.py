from rest_framework.viewsets import ModelViewSet
from apps.atracoes.models import Atracao
from apps.atracoes.api.serializers import AtracaoSerializer


class AtracaoViewSet(ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
