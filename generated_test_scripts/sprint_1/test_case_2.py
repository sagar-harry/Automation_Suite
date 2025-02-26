
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
import sys

# Setup Selenium Options
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--incognito")
options.add_argument("--disable-notifications")
options.add_argument("--disable-features=NetworkService")

# WebDriver initialization
driver = webdriver.Chrome(options=options)
driver.maximize_window()

try:
    # Open the website
    driver.get("https://saucedemo.com/")
    time.sleep(5)  # Wait for page to load

    # Login
    class LoginPage:
        def login(self, username, password):
            driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
            time.sleep(3)
            driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
            time.sleep(3)
            driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
            time.sleep(3)
    
    login_page = LoginPage()
    login_page.login("standard_user", "secret_sauce")

    # Add items to cart
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    time.sleep(3)

    # Proceed to checkout
    driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
    time.sleep(3)

    # Enter checkout information
    driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys("somename")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("lastname")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("123456")
    time.sleep(3)
    
    # Continue to payment information
    driver.find_element(By.XPATH, '//*[@id="continue"]').click()
    time.sleep(3)

    # Verify that the payment information section is displayed
    payment_information_visible = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]')
    if payment_information_visible.is_displayed():
        print("Test Passed: Payment information is visible.")
        sys.exit(0)
    else:
        print("Test Failed: Payment information is not visible.")
        sys.exit(1)

except NoSuchElementException as e:
    print(f"Test Failed: {str(e)}")
    sys.exit(1)
finally:
    # Close the driver
    driver.quit()
