# features/order_list.feature
# ---
Feature: List and filter orders
  As a pizza shop owner
  I want to be able to retrieve all the orders at once
  And I want to filter the orders by status and customer
  So that I can efficiently manage the orders

  Scenario: List all orders
    Given there are orders in the system
    When I retrieve all the orders
    Then I should see all the orders

  Scenario: Filter orders by status
    Given there are orders with different statuses in the system
    When I filter the orders by status "Delivered"
    Then I should see all the orders with status "Delivered"

  Scenario: Filter orders by customer
    Given there are orders from different customers in the system
    When I filter the orders by customer "John Doe"
    Then I should see all the orders from customer "John Doe"

# ---