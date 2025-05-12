import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pytest_bdd import scenarios, given, when, then
import time

scenarios('features/test_ui.feature')

@pytest.fixture
def browser():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://todomvc.com/examples/react/dist/")
    yield driver
    driver.quit()

@given('the todo app is open')
def open_todo_app(browser):
    pass

@when('I add a new todo "Milk"')
def add_new_todo(browser):
    new_todo_input = browser.find_element(By.CLASS_NAME, "new-todo")
    new_todo_input.send_keys("Milk")
    time.sleep(1)
    new_todo_input.send_keys(Keys.ENTER)
    time.sleep(1)

@then('the todo list should contain "Milk"')
def check_todo_exists(browser):
    todos = browser.find_elements(By.CSS_SELECTOR, ".todo-list li")
    assert any("Milk" in item.text for item in todos), "Milk not found in todo list"