import requests

def test_create_user():
    payload = {
        "title": "Leo",
        "body": "QA Engineer",
        "userId": 1
    }

    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)

    assert response.status_code == 201, f"Expected 201 - current status code: {response.status_code}"

    data = response.json()
    assert data["title"] == "Leo", f"Expected title 'Leo', got {data['title']}"
    assert data["body"] == "QA Engineer", f"Expected body 'QA Engineer', got {data['body']}"
    assert data["userId"] == 1, f"Expected userId 1, got {data['userId']}"
    assert "id" in data, "Response does not contain an 'id'"

def test_create_user_with_empty_payload():
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json={})
    assert response.status_code in [400, 422, 500, 201], f"Unexpected status code: {response.status_code}"

def test_create_user_without_json():
    response = requests.post("https://jsonplaceholder.typicode.com/posts")
    assert response.status_code in [400, 422, 500, 201], f"Unexpected status code: {response.status_code}"

def test_create_user_with_invalid_data_types():
    payload = {
        "name": 12345,
        "job": {"role": "QA"}
    }

    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)
    assert response.status_code in [400, 422, 500, 201], f"Unexpected status code: {response.status_code}"

def test_create_user_with_extremely_long_values():
    long_string = "x" * 10000

    payload = {
        "name": long_string,
        "job": long_string
    }

    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)
    assert response.status_code in [400, 422, 500, 201], f"Unexpected status code: {response.status_code}"

def test_wrong_http_method():
    payload = {
        "name": "Leo",
        "job": "QA Engineer"
    }

    response = requests.get("https://jsonplaceholder.typicode.com/posts", json=payload)
    assert response.status_code in [400, 405, 422, 500, 200], f"Unexpected status code: {response.status_code}"
