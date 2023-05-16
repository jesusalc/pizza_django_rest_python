# features/order_pizzas.feature

Feature: Order Pizzas
  As a customer
  I want to order pizzas
  So that I can enjoy my favorite food

  Scenario: Order specific flavours of pizza
    Given I have a choice of pizza flavours
    When I order a "margarita" pizza
    Then I should be able to specify the number and size of pizzas

  Scenario: Order contains customer information
    Given I am a registered customer
    When I order a pizza
    Then my information should be included in the order

  Scenario: Track the status of delivery
    Given I have ordered a pizza
    When I check my order status
    Then I should be able to track the delivery of my order

  Scenario: Order same flavour of pizza with different sizes multiple times
    Given I have a choice of pizza sizes
    When I order a "salami" pizza of "small" size
    And I order a "salami" pizza of "large" size
    Then I should be able to place the order successfully
