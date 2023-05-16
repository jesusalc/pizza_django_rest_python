from behave import given, when, then

@given('I have a choice of pizza flavours')
def step_given_i_have_a_choice_of_pizza_flavours(context):
    # Implement your setup here
    pass

@when('I order a "{flavour}" pizza')
def step_when_i_order_a_pizza(context, flavour):
    # Implement your call to the order pizza API here
    pass

@then('I should be able to specify the number and size of pizzas')
def step_then_i_should_be_able_to_specify_number_and_size(context):
    # Implement your assertion here
    pass

# Implement the other steps similarly
