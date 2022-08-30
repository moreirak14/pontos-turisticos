from rest_framework.viewsets import ModelViewSet

from apps.core.api.serializers import PontoTuristicoSerializer
from apps.core.models import PontoTuristico


class PontoTuristicoViewSet(ModelViewSet):
    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
