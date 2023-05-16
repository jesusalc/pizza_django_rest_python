from django.test import TestCase
from pizza_django.models import Customer, Order, Pizza, PizzaFlavor, PizzaSize


class RemoveOrderTest(TestCase):

    def setUp(self):
        self.customer = Customer.objects.create(name="John Doe",
                                                address="123 Street")
        self.order = Order.objects.create(customer=self.customer)
        self.pizza = Pizza.objects.create(order=self.order,
                                          flavor=PizzaFlavor.MARGARITA,
                                          size=PizzaSize.MEDIUM,
                                          count=1)

    def test_remove_order(self):
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Pizza.objects.count(), 1)

        self.order.delete()

        self.assertEqual(Order.objects.count(), 0)
        self.assertEqual(Pizza.objects.count(), 0)
