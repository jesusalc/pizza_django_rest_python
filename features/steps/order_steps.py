# features/steps/order_steps.py
from behave import given, when, then
from rest_framework.test import APIClient
from django.urls import reverse

client = APIClient()

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


@given(u'I am on the order page')
def step_impl(context):
    context.url = reverse('order-list')  # replace 'order-list' with your actual order list URL name

@when(u'I select "{flavour}" flavour')
def step_impl(context, flavour):
    context.flavour = flavour

@when(u'I select {number} pizzas')
def step_impl(context, number):
    context.number = int(number)

@when(u'I select "{size}" size')
def step_impl(context, size):
    context.size = size

@then(u'I should see "{number} {size} {flavour} pizzas" in my cart')
def step_impl(context, number, size, flavour):
    response = client.post(context.url, {'flavour': flavour, 'number': number, 'size': size})
    assert response.status_code == 201, "Failed to create order"
    context.order_id = response.json()['id']

    response = client.get(f"{context.url}{context.order_id}/")
    assert response.status_code == 200, "Failed to retrieve order"
    order = response.json()
    assert order['flavour'] == flavour, "Flavour does not match"
    assert order['number'] == number, "Number does not match"
    assert order['size'] == size, "Size does not match"

