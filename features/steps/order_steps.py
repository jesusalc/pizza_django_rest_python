# features/steps/order_steps.py
from behave import given, when, then
from rest_framework.test import APIClient
from django.urls import reverse

client = APIClient()

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

