from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'purchaser': reverse('purchaser-list', request=request, format=format),
        'purchaser/<int:pk>': reverse('purchaser-detail', request=request, format=format, kwargs={'pk': 1}),
        'purchaser/<int:pk>/product': reverse('purchaser-history', request=request, format=format, kwargs={'pk': 1}),
        'product': reverse('product-list', request=request, format=format),
        'product/<int:pk>': reverse('product-detail', request=request, format=format, kwargs={'pk': 1}),
        'purchaser-product': reverse('history-list', request=request, format=format),
    })

