# order.feature
Feature: Order pizzas
  As a customer
  I want to specify the desired flavours of pizza, the number of pizzas and their size
  So that I can order my favorite pizzas

  Scenario: Order different flavours and sizes of pizza
    Given I am on the order page
    When I select "margarita" flavour
    And I select 2 pizzas
    And I select "medium" size
    Then I should see "2 medium margarita pizzas" in my cart

    When I select "marinara" flavour
    And I select 3 pizzas
    And I select "large" size
    Then I should see "3 large marinara pizzas" in my cart

    When I select "salami" flavour
    And I select 1 pizza
    And I select "small" size
    Then I should see "1 small salami pizza" in my cart


