
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-features=NetworkService")

# Initialize the Chrome driver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Navigate to the website
    driver.get("https://saucedemo.com/")
    time.sleep(5)  # Wait for 5 seconds after opening the page
    driver.maximize_window()

    # Define login details
    username = "standard_user"
    password = "secret_sauce"

    # Log in to the UI using LoginPage class method
    class LoginPage:
        def login(self):
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]'))
            ).send_keys(username)
            time.sleep(3)  # Wait before action
            
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))
            ).send_keys(password)
            time.sleep(3)  # Wait before action

            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="login-button"]'))
            ).click()
            time.sleep(3)  # Wait before action
    
    login_page = LoginPage()
    login_page.login()

    # Wait and add 'Bike Light' to the cart
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
    ).click()
    time.sleep(3)  # Wait before action

    # Wait and add 'Fleece Jacket' to the cart
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
    ).click()
    time.sleep(3)  # Wait before action

    # Verify cart badge count
    cart_count_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
    )
    cart_count = cart_count_element.text
    
    assert cart_count == '2', f"Cart count is {cart_count}, expected '2'"

    # Take screenshot of the completed test
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\cart_test_result.png")

    sys.exit(0)  # Exit with status 0 if passed

except Exception as e:
    # Take screenshot on failure
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\cart_test_failure.png")
    print(e)
    sys.exit(1)

finally:
    # Close the driver
    driver.quit()
