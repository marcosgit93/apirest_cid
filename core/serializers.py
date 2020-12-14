from rest_framework import serializers

from core.models import Cadastro


class CoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cadastro
        fields = [
            "cid_Numero",
            "cid_Descricao",
        ]