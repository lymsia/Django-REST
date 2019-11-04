from core.models import Purchaser, Product, History
from datetime import datetime
from purchases.serializer.purchaser import PurchaserSerializer
from purchases.serializer.product import ProductSerializer
from rest_framework import serializers

class TimestampField(serializers.DateTimeField):
    """
    Convert a django datetime to/from timestamp.
    """
    def to_representation(self, value):
        """
        Convert the field to its internal representation (aka timestamp)
        :param value: the DateTime value
        :return: a UTC timestamp integer
        """
        return datetime.timestamp(value)

    def to_internal_value(self, value):
        """
        deserialize a timestamp to a DateTime value
        :param value: the timestamp value
        :return: a django DateTime value
        """
        return datetime.fromtimestamp(float('%s' % value))


class HistorySerializer(serializers.HyperlinkedModelSerializer):
    purchaser = PurchaserSerializer(read_only=True)
    product = ProductSerializer(read_only=True)
    purchaser_id = serializers.IntegerField(write_only=True)
    product_id = serializers.IntegerField(write_only=True)
    purchase_timestamp = TimestampField(source='created_at', required=False)

    class Meta:
        model = History
        fields = ['purchaser', 'product', 'purchaser_id', 'product_id', 'purchase_timestamp']

    def validate_purchaser_id(self, value):
        if Purchaser.objects.filter(id=value).count() < 1:
            raise serializers.ValidationError('Purchaser object does not exists')
        return value

    def validate_product_id(self, value):
        if Product.objects.filter(id=value).count() < 1:
            raise serializers.ValidationError('Product object does not exists')
        return value

