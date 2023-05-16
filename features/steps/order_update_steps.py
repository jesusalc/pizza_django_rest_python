# features/steps/order_update_steps.py
# -----
from behave import given, when, then
from pizza_django.models import Order, Pizza, PizzaFlavor, PizzaSize, OrderStatus

@given(u'I have a pizza order with id "{order_id}"')
def step_impl(context, order_id):
    context.order = Order.objects.get(pk=order_id)

@when('I update the pizza flavor to "{flavor}" and count to "{count}" and size to "{size}"')
def step_impl(context, flavor, count, size):
    assert context is not None, "Expected a context, but got none"
    assert flavor is not None, "Expected a flavor, but got none"
    assert count is not None, "Expected a count, but got none"
    assert size is not None, "Expected a size, but got none"
    # pizza = context.order.pizzas.first()
    pizza = context.pizza
    assert pizza is not None, "Expected a Pizza, but got none"
    pizza.flavor = flavor
    pizza.count = int(count)
    pizza.size = size
    pizza.save()
    context.pizza = pizza 

@then(u'the updated order should have flavor "{flavor}", count "{count}", and size "{size}"')
def step_impl(context, flavor, count, size):
    pizza = context.order.pizzas.first()
    assert pizza.flavor == flavor, f"Expected flavor {flavor}, but got {pizza.flavor}"
    assert pizza.count == int(count), f"Expected count {count}, but got {pizza.count}"
    assert pizza.size == size, f"Expected size {size}, but got {pizza.size}"

@given(u'I have a delivered pizza order with id "{order_id}"')
def step_impl(context, order_id):
    context.order = Order.objects.get(pk=order_id)
    context.order.status = OrderStatus.DELIVERED
    context.order.save()

@when(u'I try to update the pizza flavor to "{flavor}" and count to "{count}" and size to "{size}"')
def step_impl(context, flavor, count, size):
    try:
        pizza = context.order.pizzas.first()
        pizza.flavor = flavor
        pizza.count = int(count)
        pizza.size = size
        pizza.save()
    except Exception as e:
        context.error = str(e)

@then(u'I should get an error message')
def step_impl(context):
    assert context.error is not None, "Expected an error message, but got none"

@when(u'I change the delivery status to "{status}"')
def step_impl(context, status):
    context.order.status = status
    context.order.save()

@then(u'the updated order should have delivery status "{status}"')
def step_impl(context, status):
    assert context.order.status == status, f"Expected status {status}, but got {context.order.status}"

# -----


