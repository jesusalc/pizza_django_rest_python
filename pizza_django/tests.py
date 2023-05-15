# tests.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from pizza_django.models import Customer, Pizza, Order
from pizza_django.serializers import OrderSerializer


class OrderAPITestCase(APITestCase):
    def setUp(self):
        self.customer = Customer.objects.create(name="John Doe", address="123 Test St")
        self.pizza = Pizza.objects.create(name="Margherita", size=Pizza.SizeChoices.MEDIUM)
        self.order = Order.objects.create(customer=self.customer, delivery_status=Order.DeliveryStatusChoices.PENDING)
        self.order.pizzas.add(self.pizza)

    def test_retrieve_order(self):
        """
        Ensure we can retrieve a single order by id.
        """
        url = reverse('order-detail', kwargs={'pk': self.order.id})
        response = self.client.get(url)

        # Check that the response has a 200 status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that the returned data matches the order data
        serializer = OrderSerializer(self.order)
        self.assertEqual(response.data, serializer.data)

