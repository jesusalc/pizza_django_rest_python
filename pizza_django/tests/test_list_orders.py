from django.test import TestCase
from pizza_django.models import Customer, Order, Pizza, PizzaFlavor, PizzaSize, OrderStatus

class ListOrdersTest(TestCase):
    def setUp(self):
        self.customer1 = Customer.objects.create(name='John Doe', address='123 Main St')
        self.order1 = Order.objects.create(customer=self.customer1, status=OrderStatus.ORDERED)
        self.pizza1 = Pizza.objects.create(order=self.order1, flavor=PizzaFlavor.MARGARITA, size=PizzaSize.MEDIUM, count=1)

        self.customer2 = Customer.objects.create(name='Jane Doe', address='456 Main St')
        self.order2 = Order.objects.create(customer=self.customer2, status=OrderStatus.ORDERED)
        self.pizza2 = Pizza.objects.create(order=self.order2, flavor=PizzaFlavor.SALAMI, size=PizzaSize.LARGE, count=2)

        # Update the status of order2 to DELIVERED after the pizza has been created
        self.order2.status = OrderStatus.DELIVERED
        self.order2.save()
         
    def test_list_all_orders(self):
        all_orders = Order.objects.all()

        self.assertEqual(all_orders.count(), 2)
        self.assertIn(self.order1, all_orders)
        self.assertIn(self.order2, all_orders)

    def test_filter_orders_by_customer(self):
        john_orders = Order.objects.filter(customer=self.customer1)

        self.assertEqual(john_orders.count(), 1)
        self.assertIn(self.order1, john_orders)
        self.assertNotIn(self.order2, john_orders)

    def test_filter_orders_by_status(self):
        delivered_orders = Order.objects.filter(status=OrderStatus.DELIVERED)

        self.assertEqual(delivered_orders.count(), 1)
        self.assertIn(self.order2, delivered_orders)
        self.assertNotIn(self.order1, delivered_orders)
