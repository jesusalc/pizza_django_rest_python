# features/order_pizzas.feature

Feature: Order pizzas

  Scenario: Order a pizza
    Given I am a registered customer
    When I order a "margarita" pizza of "medium" size and "2" quantity
    Then my order should be placed successfully

  Scenario: Order contains customer information
    Given I am a registered customer
    When I order a pizza
    Then my information should be included in the order

  Scenario: Track the status of delivery
    Given I have ordered a pizza
    When I check my order status
    Then I should be able to track the delivery of my order

  Scenario: Order same flavour of pizza with different sizes multiple times
    Given I am a registered customer
    When I order a "salami" pizza of "small" size and "1" quantity
    And I order a "salami" pizza of "large" size and "1" quantity
    Then I should be able to place the order successfully
