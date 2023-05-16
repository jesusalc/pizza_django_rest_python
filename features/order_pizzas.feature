# features/order_pizzas.feature
# ---

Feature: Order pizzas

  Scenario: Specify desired flavours, count and sizes of pizza
    Given I am a registered customer
    When I order a "salami" pizza of "small" size and "2" count
    Then I should be able to place the order successfully

  Scenario: An order contains customer information
    Given I am a registered customer
    When I order a pizza
    Then my information should be included in the order

  Scenario: Track the status of delivery
    Given I am a registered customer
    And I have ordered a pizza
    When I check my order status
    Then I should be able to track the delivery of my order

  Scenario: Order same flavour of pizza with different sizes multiple times
    Given I am a registered customer
    And I have a choice of pizza sizes
    When I order a "salami" pizza of "small" size and "2" count
    And I order a "salami" pizza of "large" size and "3" count
    Then I should be able to place the order successfully


# ---