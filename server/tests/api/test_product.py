from django.test import TestCase
from rest_framework.test import APIClient
from core.models import Product


class ProductTestCase(TestCase):
    base_url = 'http://localhost:8080/api/'
    c = APIClient()

    def test_list_product(self):
        response = self.c.get(self.base_url + 'product/')
        self.assertEqual(response.status_code, 200)

    def test_create_product(self):
        response = self.c.post(self.base_url + 'product/', {'name': 'apple'}, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Product.objects.filter(name='apple').count(), 1)

    def test_update_product(self):
        user = Product.objects.create(name='orange')
        response = self.c.put(self.base_url + 'product/{}/'.format(user.id), {
            'name': 'kiwi'}, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Product.objects.filter(name='kiwi').count(), 1)

    def test_delete_product(self):
        user = Product.objects.create(name='banana')
        response = self.c.delete(self.base_url + 'product/{}/'.format(user.id))
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Product.objects.filter(name='banana').count(), 0)
