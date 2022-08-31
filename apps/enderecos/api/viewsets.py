from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from apps.enderecos.api.serializers import EnderecoSerializer
from apps.enderecos.models import Endereco


class EnderecoViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
