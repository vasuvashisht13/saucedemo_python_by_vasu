from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_saucedemo_title():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)

    # Logging in
    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")
    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    # Wait for the title element to be present
    title_element = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='title']")))

    # Verify the text of the title element
    assert title_element.text == "Products", f"Expected 'Products' but got '{title_element.text}'"

    print("Test passed! 'Products' is displayed as expected.")

    driver.quit()


test_saucedemo_title()
