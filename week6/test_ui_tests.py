
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
@pytest.fixture
def driver():
    driver = webdriver.Chrome()

def test_add_item(driver):
    driver.get("")

    driver.find_element(By.ID, "")
    driver.find_element(By.CSS_SELECTOR, "#id element").click(  )
    assert driver.find_elemnt(By.CSS_SELECTOR, "#").text() == "test"