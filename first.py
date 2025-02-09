from selenium import webdriver

def test_google_search():
    driver = webdriver.Chrome()  # Use webdriver.Firefox() for Firefox
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    driver.quit()
