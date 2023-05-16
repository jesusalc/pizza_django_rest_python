from django.test import TestCase
from pizza_django.models import Customer, Order, Pizza, PizzaFlavor, PizzaSize


class RetrieveOrderTest(TestCase):

    def setUp(self):
        self.customer = Customer.objects.create(name="John Doe",
                                                address="123 Street")
        self.order = Order.objects.create(customer=self.customer)
        self.pizza = Pizza.objects.create(order=self.order,
                                          flavor=PizzaFlavor.MARGARITA,
                                          size=PizzaSize.MEDIUM,
                                          count=1)

    def test_retrieve_order(self):
        retrieved_order = Order.objects.get(id=self.order.id)

        self.assertEqual(retrieved_order, self.order)
        self.assertEqual(retrieved_order.customer, self.customer)

        retrieved_pizza = retrieved_order.pizzas.first()

        self.assertEqual(retrieved_pizza, self.pizza)
        self.assertEqual(retrieved_pizza.flavor, PizzaFlavor.MARGARITA)
        self.assertEqual(retrieved_pizza.size, PizzaSize.MEDIUM)
        self.assertEqual(retrieved_pizza.count, 1)
