from rest_framework.viewsets import ModelViewSet
from apps.enderecos.models import Endereco
from apps.enderecos.api.serializers import EnderecoSerializer


class EnderecoViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
