from behave import given, when, then
from pizza_django.models  import Order

@given('I have placed an order')
def step_given_placed_order(context):
    context.order = Order(context.customer)  # assuming context.customer is defined elsewhere
    context.order_id = context.order.id  # assuming each order has a unique ID

@when('I decide to remove my order')
def step_when_remove_order(context):
    context.order_removed = context.order.remove_order(context.order_id)  # assuming remove_order method exists

@then('my order should be successfully removed')
def step_then_order_removed(context):
    assert context.order_removed
