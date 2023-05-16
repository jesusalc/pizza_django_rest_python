# features/order_update.feature
# --

Feature: Update an order

  Scenario: Update an order's details
    Given I have placed an order with a pizza
    When I update the pizza flavor to "Marinara" and count to "2" and size to "large"
    Then the updated order should have flavor "Marinara", count "2", and size "large"
    
  Scenario: It should not be possible to update an order for some statuses of delivery
    Given I have placed an order with a pizza and status "Delivered"
    When I try to update the pizza flavor to "Marinara" and count to "2" and size to "large"
    Then I should receive an error message that the order cannot be updated

  Scenario: Change the status of delivery
    Given I have placed an order with a pizza and status "Ordered"
    When I change the order status to "Delivered"
    Then the order status should be "Delivered"


# --