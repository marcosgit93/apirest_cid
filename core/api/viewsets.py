from rest_framework import viewsets
from core.models import Cid
from core.api.serializers import CidSerializer

class CidViewSet(viewsets.ModelViewSet):
    queryset = Cid.objects.all()
    serializer_class = CidSerializer
    