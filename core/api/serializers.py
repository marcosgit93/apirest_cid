from rest_framework import serializers
from core.models import Cid


class CidSerializer(serializers.ModelSerializer):
	
    class Meta:
        model = Cid
        fields = ('__all__')