from selenium.webdriver.common.by import By

class CheckoutCompletePage:
    def __init__(self, driver):
        self.driver = driver
        self.order_confirmation = (By.XPATH, "//h2[contains(text(), 'Thank you for your order!')]")

    def verify_order_confirmation(self):
        return "Thank you for your order!" in self.driver.find_element(*self.order_confirmation).text
