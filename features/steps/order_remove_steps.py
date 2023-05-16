# features/steps/order_remove_steps.py
# ---

from behave import given, when, then
from pizza_django.models  import Order, Customer

@given('I am a registered customer with no prior orders')
def step_given_registered_customer(context):
    context.customer = Customer.objects.create(name="Test Customer", address="123 Street")
    assert context.customer is not None

@given('I have placed an order')
def step_given_placed_order(context):
    context.order = Order(context.customer)
    context.order_id = context.order.id

@when('I decide to remove my order')
def step_when_remove_order(context):
    context.order_removed = context.order.remove_order(context.order_id)

@then('my order should be successfully removed')
def step_then_order_removed(context):
    assert context.order_removed


# ---
