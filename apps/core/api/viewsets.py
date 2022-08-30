from rest_framework.viewsets import ModelViewSet
from apps.core.models import PontoTuristico
from apps.core.api.serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
