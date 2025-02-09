import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_step_two_page import CheckoutStepTwoPage
from pages.checkout_complete_page import CheckoutCompletePage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_complete_checkout(driver):
    # Login
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    # Add product to cart
    products_page = ProductsPage(driver)
    products_page.add_backpack_to_cart()
    products_page.go_to_cart()

    # Proceed to checkout
    cart_page = CartPage(driver)
    cart_page.proceed_to_checkout()

    # Enter checkout details
    checkout_page = CheckoutPage(driver)
    checkout_page.enter_shipping_details("Vasu", "Vashisht", "141401")
    checkout_page.continue_checkout()

    # Complete checkout
    checkout_step_two_page = CheckoutStepTwoPage(driver)
    checkout_step_two_page.finish_checkout()

    # Verify order completion
    checkout_complete_page = CheckoutCompletePage(driver)
    assert checkout_complete_page.verify_order_confirmation()
