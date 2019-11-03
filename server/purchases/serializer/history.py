from core.models.history import History
from rest_framework import serializers


class HistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = History
        fields = ['purchaser', 'product', 'purchase_timestamp']

