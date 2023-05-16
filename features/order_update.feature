Feature: Update an order

  Scenario: Update an order's details
    Given I have a pizza order with id "1"
    When I update the pizza flavor to "Marinara" and count to "2" and size to "large"
    Then the updated order should have flavor "Marinara", count "2", and size "large"

  Scenario: Update a delivered order's details
    Given I have a delivered pizza order with id "1"
    When I try to update the pizza flavor to "Salami" and count to "3" and size to "medium"
    Then I should get an error message

  Scenario: Change the status of delivery
    Given I have a pizza order with id "1"
    When I change the delivery status to "Delivered"
    Then the updated order should have delivery status "Delivered"
