from django.test import TestCase
from pizza_django.models import Customer, Order, Pizza, PizzaSize, PizzaFlavor, OrderStatus

class UpdateOrderTest(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(name="Test Customer", address="123 Pizza St.")
        self.order = Order.objects.create(customer=self.customer, status=OrderStatus.ORDERED)
        self.pizza = Pizza.objects.create(
            order=self.order,
            flavor=PizzaFlavor.MARGARITA,
            size=PizzaSize.SMALL,
            count=2
        )

    def test_update_order_details(self):
        self.pizza.flavor = PizzaFlavor.MARINARA
        self.pizza.size = PizzaSize.LARGE
        self.pizza.count = 3
        self.pizza.save()

        updated_pizza = Pizza.objects.get(id=self.pizza.id)
        self.assertEqual(updated_pizza.flavor, PizzaFlavor.MARINARA)
        self.assertEqual(updated_pizza.size, PizzaSize.LARGE)
        self.assertEqual(updated_pizza.count, 3)

    def test_not_update_delivered_order(self):
        self.order.status = OrderStatus.DELIVERED
        self.order.save()

        with self.assertRaises(Exception):
            self.pizza.flavor = PizzaFlavor.SALAMI
            self.pizza.save()

    def test_change_delivery_status(self):
        self.order.status = OrderStatus.DELIVERED
        self.order.save()

        updated_order = Order.objects.get(id=self.order.id)
        self.assertEqual(updated_order.status, OrderStatus.DELIVERED)
