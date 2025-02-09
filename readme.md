Project: SauceDemo Checkout Automation
This project automates the end-to-end purchase flow on SauceDemo using Selenium WebDriver and Python (Pytest). It follows the Page Object Model (POM) to enhance maintainability and scalability.

Features:
✅ Login Automation – Logs in with valid credentials.
✅ Product Selection – Adds the Sauce Labs Backpack to the cart.
✅ Cart Management – Navigates to the cart and proceeds to checkout.
✅ Checkout Process – Fills in shipping details and completes the purchase.
✅ Order Confirmation Validation – Verifies the success message: "Thank you for your order!"
✅ Test Reporting – Generates HTML reports using Pytest.

Technologies Used:
🔹 Python 🐍
🔹 Selenium WebDriver 🌐
🔹 Pytest 📌
🔹 Page Object Model (POM) 🏗️


How to Run:
Install dependencies
pip install -r requirements.txt


Execute the test
pytest tests/test_checkout.py --html=reports/checkout_report.html --self-contained-html
