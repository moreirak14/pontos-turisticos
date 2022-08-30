from rest_framework.viewsets import ModelViewSet

from apps.core.api.serializers import PontoTuristicoSerializer
from apps.core.models import PontoTuristico


class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        id = self.request.query_params.get("id", None)
        nome = self.request.query_params.get("nome", None)
        descricao = self.request.query_params.get("id", None)

        if id is not None:
            return PontoTuristico.objects.filter(id=id)

        if nome is not None:
            return PontoTuristico.objects.filter(nome__iexact=nome)

        if descricao is not None:
            return PontoTuristico.objects.filter(descricao__iexact=descricao)

        return PontoTuristico.objects.all()
