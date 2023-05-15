# features/steps/order_steps.py
from behave import given, when, then
from behave.runner import Context

from django.test import Client
import json

@given('an order')
def step_given_an_order(context: Context):
    context.client = Client()
    context.order = {
        "flavour": "margarita",
        "size": "medium",
        "count": 2,
        "customer": 1,
        "status": "preparing"
    }

@when('the order is submitted')
def step_when_order_submitted(context: Context):
    response = context.client.post('/api/orders/', data=json.dumps(context.order), content_type='application/json')
    context.response = response

@then('the order is created successfully')
def step_then_order_created_successfully(context: Context):
    assert context.response.status_code == 201

@then('the order details are correct')
def step_then_order_details_correct(context: Context):
    response_data = json.loads(context.response.content)
    assert response_data['flavour'] == context.order['flavour']
    assert response_data['size'] == context.order['size']
    assert response_data['count'] == context.order['count']
    assert response_data['customer'] == context.order['customer']
    assert response_data['status'] == context.order['status']


