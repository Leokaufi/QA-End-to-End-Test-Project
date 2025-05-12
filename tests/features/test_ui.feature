Feature: Todo app UI test

  Scenario: Add todo item
    Given the todo app is open
    When I add a new todo "Milk"
    Then the todo list should contain "Milk"
