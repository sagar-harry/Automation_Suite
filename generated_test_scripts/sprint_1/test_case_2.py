
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure ChromeOptions
options = Options()
options.add_argument("--disable-notifications")
options.add_argument("--incognito")
options.add_argument("--disable-features=NetworkService")

try:
    # Initialize WebDriver
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)

    # Navigate to the website
    driver.get("https://saucedemo.com/")
    time.sleep(5)  # Wait for 5 seconds after page opens
    driver.maximize_window()

    # LoginPage class with login method
    class LoginPage:
        def __init__(self, driver):
            self.driver = driver

        def login(self, username, password):
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]'))).send_keys(username)
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]'))).send_keys(password)
            time.sleep(3)  # Wait for 3 seconds before clicking login
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]'))).click()

    # Log into the application
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    # Add Bike Light to cart
    time.sleep(3)  # Wait for 3 seconds
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()

    # Add Fleece Jacket to cart
    time.sleep(3)  # Wait for 3 seconds
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))).click()

    # Navigate to the cart
    time.sleep(3)  # Wait for 3 seconds
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="shopping_cart_container"]/a'))).click()

    # Proceed to checkout
    time.sleep(3)  # Wait for 3 seconds
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkout"]'))).click()

    # Enter checkout information
    time.sleep(3)  # Wait for 3 seconds
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="first-name"]'))).send_keys("Jonnathan")
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="last-name"]'))).send_keys("K")
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="postal-code"]'))).send_keys("10007")
    time.sleep(3)  # Wait for 3 seconds
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="continue"]'))).click()

    # Check if the Payment Information label is displayed
    time.sleep(3)  # Wait for 3 seconds
    if wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]'))):
        print("Payment Information is visible. Test Passed.")
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\payment_info_visible.png")
        sys.exit(0)  # Test case passed
    else:
        print("Payment Information is not visible. Test Failed.")
        sys.exit(1)  # Test case failed

except Exception as e:
    print(f"Test Failed due to an exception: {e}")
    sys.exit(1)
finally:
    # Close the browser
    driver.quit()
