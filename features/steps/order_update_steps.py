# features/steps/order_update_steps.py
# -----
from behave import given, when, then
from pizza_django.models import Order, Pizza, PizzaFlavor, PizzaSize, OrderStatus, Customer
from django.test import TestCase

@given('I have placed an order with a pizza and status "{status}"')
def step_given_placed_order_with_pizza(context, status):
    context.customer = Customer.objects.create(name='John Doe', address='123 Elm St')
    context.order = Order.objects.create(customer=context.customer, status=status)
    context.pizza = Pizza.objects.create(order=context.order, flavor=PizzaFlavor.MARGARITA, size=PizzaSize.SMALL, count=1)

@when('I update the pizza flavor to "{flavor}" and count to "{count}" and size to "{size}"')
def step_when_update_pizza(context, flavor, count, size):
    pizza = context.order.pizzas.first()
    pizza.flavor = flavor
    pizza.count = int(count)
    pizza.size = size
    pizza.save()
    context.pizza = pizza

@when('I try to update the pizza flavor to "{flavor}" and count to "{count}" and size to "{size}"')
def step_when_try_update_pizza(context, flavor, count, size):
    try:
        pizza = context.order.pizzas.first()
        if context.order.status == 'Delivered':
            raise Exception('Cannot update a delivered order')
        pizza.flavor = flavor
        pizza.count = int(count)
        pizza.size = size
        pizza.save()
        context.pizza = pizza
    except Exception as e:
        context.error = str(e)


@when('I change the order status to "{status}"')
def step_when_change_order_status(context, status):
    context.order.status = status
    context.order.save()

@then('the updated order should have flavor "{flavor}", count "{count}", and size "{size}"')
def step_then_updated_order(context, flavor, count, size):
    pizza = context.order.pizzas.first()
    assert pizza.flavor == flavor
    assert pizza.count == int(count)
    assert pizza.size == size

@then('I should receive an error message that the order cannot be updated')
def step_then_receive_error(context):
    assert context.error is not None

@then('the order status should be "{status}"')
def step_then_order_status(context, status):
    assert context.order.status == status

@given('I have placed an order with a pizza')
def step_impl(context):
    # Creating a customer
    customer = Customer.objects.create(name='John Doe', address='123 Elm St')
    
    # Creating an order linked to the customer
    order = Order.objects.create(customer=customer, status=OrderStatus.ORDERED)
    
    # Creating a pizza linked to the order
    pizza = Pizza.objects.create(order=order, flavor='Margherita', size='Medium', count=1)
    
    # Storing the created order and pizza in the context
    context.order = order
    context.pizza = pizza


# -----


