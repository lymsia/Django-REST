from core.models.purchaser import Purchaser
from rest_framework import serializers


class PurchaserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Purchaser
        fields = ['name']

