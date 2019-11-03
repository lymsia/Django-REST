
def history_accumulator(acc, history):
    dt_format = '%Y-%M-%d'
    if history.purchase_timestamp.strftime(dt_format) in acc:
        acc[history.purchase_timestamp.strftime(dt_format)].append({'product': history.product.name})
    else:
        acc[history.purchase_timestamp.strftime(dt_format)] = [{'product': history.product.name}]
    return acc

