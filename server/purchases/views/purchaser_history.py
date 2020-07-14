from functools import reduce
from purchases.library.common import query_history, history_accumulator
from rest_framework import generics
from rest_framework.response import Response


class PurchaserHistory(generics.GenericAPIView):

    def get(self, request, pk):
        # initialize
        start_date = request.GET.get('start_date', None)
        end_date = request.GET.get('end_date', None)

        # query to db
        historys = query_history(pk, start_date, end_date)

        return Response({
            'purchases': reduce(history_accumulator, historys, {})
        })
