
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import sys

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-features=NetworkService")

# Instantiate the WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Maximize the window
driver.maximize_window()

# Define LoginPage class
class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        username_field = self.driver.find_element(By.XPATH, '//*[@id="user-name"]')
        password_field = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        login_button = self.driver.find_element(By.XPATH, '//*[@id="login-button"]')

        username_field.send_keys(username)
        time.sleep(3)

        password_field.send_keys(password)
        time.sleep(3)

        login_button.click()
        time.sleep(3)

try:
    # Open the website
    driver.get("https://saucedemo.com/")
    time.sleep(5)

    # Login to website
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    # Add Bike Light to cart
    bike_light_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
    bike_light_button.click()
    time.sleep(3)

    # Add Fleece Jacket to cart
    fleece_jacket_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
    fleece_jacket_button.click()
    time.sleep(3)

    # Verify the cart badge count
    cart_count_badge = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    cart_count = cart_count_badge.text

    # Check if cart count is '2'
    assert cart_count == '2', f"Cart count is not as expected, found: {cart_count}"
    
    # Save the snapshot of the page
    driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot.png")

    # Close the driver
    driver.quit()

    # Exit with success code
    sys.exit(0)

except Exception as e:
    # Save the snapshot of the page in case of failure
    driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot_failed.png")
    
    # Print exception and exit with failure code
    print(f"Test failed due to: {e}")
    driver.quit()
    sys.exit(1)
