Feature: Create user via API

  Scenario: Successful user creation
    Given I have a valid API endpoint
    When I send a POST request with valid user data
    Then the API should respond with status code 201

