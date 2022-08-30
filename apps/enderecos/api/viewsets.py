from rest_framework.viewsets import ModelViewSet

from apps.enderecos.api.serializers import EnderecoSerializer
from apps.enderecos.models import Endereco


class EnderecoViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
