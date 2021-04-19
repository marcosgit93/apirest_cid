from rest_framework import viewsets
from core.models import Cid
from core.api.serializers import CidSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class CidViewSet(viewsets.ModelViewSet):
    queryset = Cid.objects.all()
    serializer_class = CidSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)