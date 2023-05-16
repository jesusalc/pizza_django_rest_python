# features/steps/order_retrieve_steps.py
# ---

from behave import given, when, then
from pizza_django.models import Customer, Order


@given('I am a registered customer with no orders')
def step_given_registered_customer(context):
    context.customer = Customer.objects.create(name="Test Customer",
                                               address="123 Street")
    assert context.customer is not None


@given('I have placed an order to retrieve')
def step_given_placed_order(context):
    context.customer = Customer.objects.create(name='John Doe',
                                               address='123 Abc St.')
    context.order = Order.objects.create(customer=context.customer)
    context.order_id = context.order.id
    assert context.customer is not None
    assert context.order is not None
    assert context.order_id is not None


@when('I retrieve the order by its identifier')
def step_when_retrieve_order(context):
    context.retrieved_order = Order.objects.get(id=context.order_id)


@then('I should be able to see the details of my order')
def step_then_see_order_details(context):
    assert context.retrieved_order.id == context.order_id


# ---
