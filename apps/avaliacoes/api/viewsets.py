from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from apps.avaliacoes.api.serializers import AvalicaoSerializer
from apps.avaliacoes.models import Avaliacao


class AvaliacaoViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Avaliacao.objects.all()
    serializer_class = AvalicaoSerializer
