from django.test import TestCase
from rest_framework.test import APIClient
from core.models import Purchaser


class PurchaserTestCase(TestCase):
    base_url = 'http://localhost:8080/api/'
    c = APIClient()

    def test_list_purchaser(self):
        response = self.c.get(self.base_url + 'purchaser/')
        self.assertEqual(response.status_code, 200)

    def test_create_purchaser(self):
        response = self.c.post(self.base_url + 'purchaser/', {'name': 'user1'}, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Purchaser.objects.filter(name='user1').count(), 1)

    def test_update_purchaser(self):
        user = Purchaser.objects.create(name='user2')
        response = self.c.put(self.base_url + 'purchaser/{}/'.format(user.id), {
            'name': 'user3'}, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Purchaser.objects.filter(name='user3').count(), 1)

    def test_delete_purchaser(self):
        user = Purchaser.objects.create(name='user4')
        response = self.c.delete(self.base_url + 'purchaser/{}/'.format(user.id))
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Purchaser.objects.filter(name='user4').count(), 0)
