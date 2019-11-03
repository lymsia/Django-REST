import datetime
from core.models import History


def history_accumulator(acc, history):
    dt_format = '%Y-%m-%d'
    if history.purchase_timestamp.strftime(dt_format) in acc:
        acc[history.purchase_timestamp.strftime(dt_format)].append({'product': history.product.name})
    else:
        acc[history.purchase_timestamp.strftime(dt_format)] = [{'product': history.product.name}]
    return acc

def query_history(pk, start_date, end_date):
    dt_format = '%Y-%m-%d'
    dt_end_date_format = '%Y-%m-%d %H:%M:%S'
    if start_date and end_date:
        end_date = end_date + ' 23:59:59'
        return History.objects\
            .filter(
                purchaser__id=pk,
                purchase_timestamp__range=[
                    datetime.datetime.strptime(start_date, dt_format),
                    datetime.datetime.strptime(end_date, dt_end_date_format)
                ],
            )\
            .order_by('-purchase_timestamp')\
            .select_related('purchaser', 'product')

    if start_date:
        return History.objects\
            .filter(
                purchaser__id=pk,
                purchase_timestamp__gte=datetime.datetime.strptime(start_date, dt_format)
            )\
            .order_by('-purchase_timestamp')\
            .select_related('purchaser', 'product')

    if end_date:
        end_date = end_date + ' 23:59:59'
        return History.objects\
            .filter(
                purchaser__id=pk,
                purchase_timestamp__lte=datetime.datetime.strptime(end_date, dt_end_date_format)
            )\
            .order_by('-purchase_timestamp')\
            .select_related('purchaser', 'product')

    return History.objects\
            .filter(purchaser__id=pk)\
            .order_by('-purchase_timestamp')\
            .select_related('purchaser', 'product')

