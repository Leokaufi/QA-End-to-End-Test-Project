# QA End-To-End Project

## In this project, I made automated tests for API responses, UI functionalities, and database layers. Additionally I implemented modern QA - Testing with BDD (behaviour driven developement) using Gherkin and 'pytest-bdd' syntax.

### Automated Tests

With the Python file test_api_users.py I created six different automated tests, which all tested different aspects of an API.
The tests include checking if I can successfully create an user and get the right JSON file back from the API, testing if the API will give me an error when there is no payload, no JSON file in the POST request, when there is an invalid data type such as integers or dictionaries in the payload, when there is a string that is too long, and what happens when I try to send a GET request to a POST endpoint.

With the Python file test_db_tasks.py I tested if a SQL file gets created and made sure to get the right parameters such as "pytest DB-Test" in column 1.

The last test, which is also my favourite, tests the user interface of a dummy website.
It creates a to-do list, writes text into the field, marks it as done, and closes the driver.
The test gets the list from the website, which contains all the to-dos, and checks if the text that was given by me is present.

### BDD Extension

As a final step, I implemented Behaviour Driven Developement (BDD) tests using `pytest-bdd` and Gherkin syntax.

This includes:
- An API test where test steps are described in plain English (Given-When-Then)
- A Selenium UI test that uses BDD to check the functionality of a web to-do app

With this, the project includes both classic pytest tests and modern BDD-style tests.