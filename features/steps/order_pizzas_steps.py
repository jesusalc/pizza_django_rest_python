# features/steps/order_pizzas_steps.py
# ---

from behave import given, when, then
from django.test import Client
from pizza_django.models import Order, Pizza, Customer, PizzaFlavor, PizzaSize

@given('I am a registered customer')
def step_impl(context):
    context.customer = Customer.objects.create(name="Test Customer", address="123 Street")
    assert context.customer is not None

@when('I order a "{flavor}" pizza of "{size}" size and "{count}" count')
def step_when_order_pizza(context, flavor, size, count):
    order = Order(customer=context.customer)
    order.save()
    pizza = Pizza(order=order, flavor=flavor, size=size, count=count)
    pizza.save()
    context.order = order
    assert context.order is not None
    context.order_id = order.id
    assert context.order_id is not None

@then('my order should be placed successfully')
def step_impl(context):
    assert context.order is not None
    assert context.order.status == 'OD'

@when('I order a pizza')
def step_when_order_pizza_default(context):
    step_when_order_pizza(context, PizzaFlavor.MARGARITA, PizzaSize.MEDIUM, 1)

@when('I order a medium margarita pizza')
def step_impl(context):
    context.execute_steps(f'When I order a "margarita" pizza of "medium" size and "1" quantity')

@then('my information should be included in the order')
def step_then_order_contains_customer_info(context):
    order_id = context.order.id
    order = Order.objects.get(id=order_id)
    assert order.customer == context.customer
    assert context.order.customer == context.customer

@given('I have ordered a pizza')
def step_given_ordered_pizza(context):
    step_when_order_pizza_default(context)

@given('I can order a pizza')
def step_impl(context):
    context.execute_steps('Given I am a registered customer')
    context.execute_steps('When I order a pizza')

@when('I check my order status')
def step_when_check_order_status(context):
    order_id = context.order.id
    order = Order.objects.get(id=order_id)
    context.order_status = order.status
    context.status = order.status

@then('I should be able to track the delivery of my order')
def step_then_track_delivery(context):
    assert context.order_status is not None
    assert context.status == context.order.status

@then(u'I should be able to place the order successfully')
def step_then_order_success(context):
    # def step_impl(context):
    order_id = context.order_id
    order = Order.objects.get(pk=order_id)
    assert order is not None, f"Order with id {order_id} does not exist"
    assert order.pizzas.count() > 0, "Order does not have any pizzas"

@given(u'I have a choice of pizza sizes')
def step_impl(context):
    context.pizza_sizes = [PizzaSize.SMALL, PizzaSize.MEDIUM, PizzaSize.LARGE]
    assert context.pizza_sizes is not None



# ---

