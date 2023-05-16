# features/order_retrieve.feature
# ---

Feature: Retrieve an order
  As a pizza shop customer
  I want to be able to retrieve an order by its identifier
  So that I can view the details of my order

  Scenario: Retrieve an order
    Given I am a registered customer with no orders
    And I have placed an order to retrieve
    When I retrieve the order by its identifier
    Then I should be able to see the details of my order


# ---