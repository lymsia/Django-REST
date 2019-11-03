import datetime
from core.models import History
from functools import reduce
from purchases.library.common import history_accumulator
from rest_framework import generics
from rest_framework.response import Response


class PurchaserHistory(generics.GenericAPIView):

    def get(self, request, pk):
        # initialize
        start_date = request.GET.get('start_date', None)
        end_date = request.GET.get('end_date', None)

        # query to db
        historys = History.objects\
                .filter(
                    purchaser__id=pk
                    #  purchase_timestamp__startswith >= datetime.datetime(start_date).date(),
                    #  purchase_timestamp__endswith <= datetime.datetime(end_date).date(),
                )\
                .order_by('-purchase_timestamp')\
                .select_related('purchaser', 'product')

        #  if start_date:
            #  historys.filter(purchase_timestamp >= datetime(start_date).date())
        #  if end_date:
            #  historys.filter(purchase_timestamp <= datetime(end_date).date())

        return Response({
            'purchases': reduce(history_accumulator, historys, {})
        })

