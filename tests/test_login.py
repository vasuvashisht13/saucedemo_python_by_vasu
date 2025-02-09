import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login(driver):
    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)

    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    assert products_page.get_page_title() == "Products", "Login failed, 'Products' title not found."
    print("Login Test Passed!")
