import requests
from pytest_bdd import scenarios, given, when, then

scenarios('features/test_api.feature')

API_URL = "https://jsonplaceholder.typicode.com/posts"
response = None

@given("I have a valid API endpoint")
def valid_endpoint():
    return API_URL


@when("I send a POST request with valid user data")
def send_post_request():
    global response
    payload = {
        "title": "Leo",
        "body": "QA Engineer",
        "userId": 1
    }
    response = requests.post(API_URL, json=payload)

@then("the API should respond with status code 201")
def check_response_status():
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"
