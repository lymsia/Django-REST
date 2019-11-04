from core.models import Purchaser, Product, History
from purchases.serializer.purchaser import PurchaserSerializer
from purchases.serializer.product import ProductSerializer
from rest_framework import serializers


class HistorySerializer(serializers.HyperlinkedModelSerializer):
    purchaser = serializers.PrimaryKeyRelatedField(queryset=Purchaser.objects.all())
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = History
        fields = ['purchaser', 'product', 'purchase_timestamp']

