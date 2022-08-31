from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from apps.atracoes.api.serializers import AtracaoSerializer
from apps.atracoes.models import Atracao


class AtracaoViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
