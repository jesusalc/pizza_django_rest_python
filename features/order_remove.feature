# features/order_remove.feature
# ---

Feature: Remove an order

  As a pizza shop customer
  I want to be able to remove an order
  So that I can correct any mistakes I made while ordering

  Scenario: Remove an order
    Given I am a registered customer with no prior orders
    And I have placed an order
    When I decide to remove my order
    Then my order should be successfully removed


# ---
