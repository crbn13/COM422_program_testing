
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

def setup_function(function):
    if os.path.exists("data/vehicles.json"):
        os.remove("data/vehicles.json")

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_add_item(driver):
    driver.get("http://localhost:5000")

    driver.find_element(By.ID, "txtreg").send_keys("test")
    driver.find_element(By.ID, "btnadd").click()
    assert driver.find_elements(By.ID, "spaces")[-1].text == "test"