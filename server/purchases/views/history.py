from core.models import History 
from purchases.serializer.history import HistorySerializer
from rest_framework import generics


class HistoryList(generics.ListCreateAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
