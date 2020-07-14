from core.models import Purchaser
from purchases.serializer.purchaser import PurchaserSerializer
from rest_framework import generics


class PurchaserList(generics.ListCreateAPIView):
    queryset = Purchaser.objects.all()
    serializer_class = PurchaserSerializer


class PurchaserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Purchaser.objects.all()
    serializer_class = PurchaserSerializer
