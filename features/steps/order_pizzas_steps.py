from behave import given, when, then
from django.test import Client
from pizza_django.models import Order, Pizza, Customer, PizzaFlavor, PizzaSize

@given('I am a registered customer')
def step_impl(context):
    context.customer = Customer.objects.create(name="Test Customer", address="123 Street")
    assert context.customer is not None

@when('I order a "{flavor}" pizza of "{size}" size and "{quantity}" quantity')
def step_impl(context, flavor, size, quantity):
    context.order = Order.objects.create(customer=context.customer)
    Pizza.objects.create(
        order=context.order,
        flavor=flavor,
        size=size,
        count=int(quantity),
    )

@then('my order should be placed successfully')
def step_impl(context):
    assert context.order is not None
    assert context.order.status == 'OD'

@when('I order a pizza')
def step_impl(context):
    context.execute_steps(f'When I order a "margarita" pizza of "medium" size and "1" quantity')

@then('my information should be included in the order')
def step_impl(context):
    assert context.order.customer == context.customer

@given('I have ordered a pizza')
def step_impl(context):
    context.execute_steps('Given I am a registered customer')
    context.execute_steps('When I order a pizza')

@when('I check my order status')
def step_impl(context):
    context.status = Order.objects.get(id=context.order.id).status

@then('I should be able to track the delivery of my order')
def step_impl(context):
    assert context.status == context.order.status

@then(u'I should be able to place the order successfully')
def step_impl(context):
    order_id = context.order_id
    order = Order.objects.get(pk=order_id)
    assert order is not None, f"Order with id {order_id} does not exist"
    assert order.pizzas.count() > 0, "Order does not have any pizzas"
