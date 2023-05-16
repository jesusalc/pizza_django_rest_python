from django.test import TestCase
from pizza_django.models import Customer, Order, Pizza, PizzaSize, PizzaFlavor, OrderStatus


class PizzaOrderTest(TestCase):

    def setUp(self):
        self.customer = Customer.objects.create(name="Test Customer",
                                                address="123 Pizza St.")
        self.order = Order.objects.create(customer=self.customer,
                                          status=OrderStatus.ORDERED)

    def test_order_pizza(self):
        pizza = Pizza.objects.create(order=self.order,
                                     flavor=PizzaFlavor.MARGARITA,
                                     size=PizzaSize.SMALL,
                                     count=2)
        self.assertEqual(pizza.flavor, PizzaFlavor.MARGARITA)
        self.assertEqual(pizza.size, PizzaSize.SMALL)
        self.assertEqual(pizza.count, 2)

    def test_order_contains_customer_info(self):
        self.assertEqual(self.order.customer.name, "Test Customer")
        self.assertEqual(self.order.customer.address, "123 Pizza St.")

    def test_track_delivery_status(self):
        self.assertEqual(self.order.status, OrderStatus.ORDERED)
        self.order.status = OrderStatus.DELIVERED
        self.order.save()
        self.assertEqual(self.order.status, OrderStatus.DELIVERED)

    def test_order_same_flavor_different_sizes(self):
        Pizza.objects.create(order=self.order,
                             flavor=PizzaFlavor.MARGARITA,
                             size=PizzaSize.SMALL,
                             count=1)
        Pizza.objects.create(order=self.order,
                             flavor=PizzaFlavor.MARGARITA,
                             size=PizzaSize.LARGE,
                             count=1)
        margarita_pizzas = self.order.pizzas.filter(
            flavor=PizzaFlavor.MARGARITA)
        self.assertEqual(margarita_pizzas.count(), 2)
        self.assertEqual(
            margarita_pizzas.filter(size=PizzaSize.SMALL).count(), 1)
        self.assertEqual(
            margarita_pizzas.filter(size=PizzaSize.LARGE).count(), 1)
