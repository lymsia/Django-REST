import datetime
from django.test import TestCase
from rest_framework.test import APIClient
from core.models import Purchaser, Product, History


class HistoryTestCase(TestCase):
    base_url = 'http://localhost:8080/api/'
    c = APIClient()

    def test_create_history(self):
        user = Purchaser.objects.create(name='user1')
        product = Product.objects.create(name='apple')
        response = self.c.post(self.base_url + 'purchaser-product/',
                    {
                        'purchaser_id': user.id,
                        'product_id': product.id,
                        'purchase_timestamp': datetime.datetime.now().timestamp(),
                    }, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(History.objects.all().count(), 1)

