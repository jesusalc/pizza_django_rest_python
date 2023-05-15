# tests.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.test import TestCase
from pizza_django.models import Customer, Pizza, Order
from pizza_django.serializers import OrderSerializer
from .models import Order, Customer, PizzaFlavor, PizzaSize, PizzaOrder


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


class OrderTestCase(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(name="John Doe", address="123 Street")
        self.flavor = PizzaFlavor.objects.create(name="Margarita")
        self.size = PizzaSize.objects.create(size="Medium")

    def test_order_pizzas(self):
        order = Order.objects.create(customer=self.customer, status='Ordered')
        PizzaOrder.objects.create(order=order, flavor=self.flavor, size=self.size, quantity=2)

        pizza_order = PizzaOrder.objects.get(order=order)
        self.assertEqual(pizza_order.flavor.name, 'Margarita')
        self.assertEqual(pizza_order.size.size, 'Medium')
        self.assertEqual(pizza_order.quantity, 2)

    def test_order_same_pizza_different_sizes(self):
        order = Order.objects.create(customer=self.customer, status='Ordered')
        PizzaOrder.objects.create(order=order, flavor=self.flavor, size=self.size, quantity=2)
        large_size = PizzaSize.objects.create(size="Large")
        PizzaOrder.objects.create(order=order, flavor=self.flavor, size=large_size, quantity=1)

        pizza_orders = PizzaOrder.objects.filter(order=order, flavor=self.flavor)
        self.assertEqual(pizza_orders.count(), 2)
