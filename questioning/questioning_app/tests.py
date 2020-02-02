from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse

from questioning_app.models import User, Order


class UserTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('questioning')

    def setUp(self):
        self.client.login(username='guest', password='guest')

    def test_create_user(self):
        data = {
            'first_name': 'Qwerty',
            'last_name': 'Asdfgh',
            'age': 123,
            'occupation': 'IT',
            'email': 'qwerty@qwerty.com',
            'facebook_username': 'qwerty',
        }
        users_count = User.objects.count()
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.count(), users_count + 1)

    def test_create_with_wrong_data(self):
        data = {
            'first_name': ['Qwerty'],
            'last_name': {'0': 'Asdfgh'},
            'age': 'zxc',
            'occupation': '05',
            'email': 123,
            'facebook_username': 321,
        }
        users_count = User.objects.count()
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.count(), users_count)

    def test_create_with_missed_required_data(self):
        data = {
            'email': 'qwerty@qwerty.com',
            'facebook_username': 'qwerty',
        }
        users_count = User.objects.count()
        response = self.client.post(self.url, dict())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.count(), users_count)


class OrderTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('order')

    def setUp(self):
        self.client.login(username='guest', password='guest')
        User.objects.get(username='guest').user_permissions.add(
            Permission.objects.get(codename='showcase_allowed')
        )

    def test_create_order(self):
        data = {
            'user': User.objects.get(username='guest').id,
            'products': ['1', '3'],
        }
        orders_count = Order.objects.count()
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Order.objects.count(), orders_count + 1)

    def test_create_with_wrong_data(self):
        data = {
            'user': 'qwe',
            'products': 'asd',
        }
        orders_count = Order.objects.count()
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Order.objects.count(), orders_count)

    def test_create_with_missed_required_data(self):
        orders_count = Order.objects.count()
        response = self.client.post(self.url, dict())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Order.objects.count(), orders_count)
