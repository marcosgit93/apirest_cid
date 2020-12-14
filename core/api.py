from rest_framework import viewsets

from core.models import Cadastro
from core.serializers import CoreSerializer


class CoreViewSet(viewsets.ModelViewSet):
    queryset = Cadastro.objects.all()
    serializer_class = CoreSerializergit init