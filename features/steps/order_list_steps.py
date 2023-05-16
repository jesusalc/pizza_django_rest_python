# features/steps/order_list_steps.py
# ---

from behave import given, when, then
from pizza_django.models import Customer, Order, OrderStatus

@given('there are orders in the system')
def step_given_orders_in_system(context):
    customer = Customer.objects.create(name='John Doe', address='123 Abc St.')
    context.orders = [
        Order.objects.create(customer=customer, status=OrderStatus.ORDERED),
        Order.objects.create(customer=customer, status=OrderStatus.DELIVERED),
    ]

@given('there are orders with different statuses in the system')
def step_given_orders_with_different_statuses(context):
    step_given_orders_in_system(context)

@given('there are orders from different customers in the system')
def step_given_orders_from_different_customers(context):
    context.orders = [
        Order.objects.create(customer=Customer.objects.create(name='John Doe', address='123 Abc St.')),
        Order.objects.create(customer=Customer.objects.create(name='Jane Doe', address='456 Def St.')),
    ]

@when('I retrieve all the orders')
def step_when_retrieve_all_orders(context):
    context.retrieved_orders = list(Order.objects.all())

@when('I filter the orders by status "{status}"')
def step_when_filter_orders_by_status(context, status):
    context.retrieved_orders = list(Order.objects.filter(status=status))

@when('I filter the orders by customer "{customer_name}"')
def step_when_filter_orders_by_customer(context, customer_name):
    context.retrieved_orders = list(Order.objects.filter(customer__name=customer_name))

@then('I should see all the orders')
def step_then_see_all_orders(context):
    assert len

@then('I should see all the orders with status "{status}"')
def step_then_see_all_orders_with_status(context, status):
    assert all(order.status == status for order in context.retrieved_orders)

@then('I should see all the orders from customer "{customer_name}"')
def step_then_see_all_orders_from_customer(context, customer_name):
    assert all(order.customer.name == customer_name for order in context.retrieved_orders)

@given('I have placed an order with pizzas')
def step_given_placed_order_with_pizzas(context):
    assert context is not None
    context.customer = Customer.objects.create(name='John Doe', address='123 Elm St')
    assert context.customer is not None
    context.order = Order.objects.create(customer=context.customer, status=OrderStatus.ORDERED)
    assert context.order is not None
    
    pizza1 = Pizza.objects.create(order=context.order, flavor=PizzaFlavor.MARGARITA, size=PizzaSize.SMALL, count=1)
    assert pizza1 is not None
    pizza2 = Pizza.objects.create(order=context.order, flavor=PizzaFlavor.HAWAIIAN, size=PizzaSize.MEDIUM, count=2)
    assert pizza2 is not None
    
    context.pizzas = [pizza1, pizza2]
    assert context.pizzas is not None


# ---
