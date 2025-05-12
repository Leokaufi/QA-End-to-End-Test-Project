import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

TO_DO_TEXT = "Buy milk"

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://todomvc.com/examples/react/dist/")
    time.sleep(1)
    yield driver
    driver.quit()

def test_element_in_list(driver):
    input_field = driver.find_element(By.CLASS_NAME, "new-todo")
    input_field.send_keys(TO_DO_TEXT)
    time.sleep(1)
    input_field.send_keys(Keys.ENTER)
    time.sleep(1)
    check_box = driver.find_element(By.CLASS_NAME, "toggle")
    check_box.click()
    time.sleep(1)

    todo_items = driver.find_elements(By.CSS_SELECTOR, ".todo-list li")

    assert any(TO_DO_TEXT in item.text for item in todo_items), f"{TO_DO_TEXT} not found in ToDo list"
