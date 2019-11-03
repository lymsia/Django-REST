from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'purchaser': reverse('purchaser-list', request=request, format=format),
        'product': reverse('product-list', request=request, format=format),
        'purchaser-product': reverse('purchaser-product-list', request=request, format=format),
    })

