from rest_framework.viewsets import ModelViewSet

from apps.core.api.serializers import PontoTuristicoSerializer
from apps.core.models import PontoTuristico


class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)
