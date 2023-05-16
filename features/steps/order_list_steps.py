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

# ---