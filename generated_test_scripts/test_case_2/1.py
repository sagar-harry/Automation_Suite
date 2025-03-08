
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
from compare_sentences import compare_sentences

# Setup Chrome options
options = Options()
options.add_argument("--incognito")
options.add_argument("--disable-notifications")
options.add_argument("--disable-popup-blocking")

# Initialize the Chrome driver
driver = webdriver.Chrome(options=options)

try:
    # Navigate to the SauceDemo login page
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@data-test='username']")))
    time.sleep(3)

    # Enter username
    username_input = driver.find_element(By.XPATH, "//input[@data-test='username']")
    username_input.send_keys("standard_user")
    time.sleep(3)

    # Enter password
    password_input = driver.find_element(By.XPATH, "//input[@data-test='password']")
    password_input.send_keys("secret_sauce")
    time.sleep(3)

    # Click the login button
    login_button = driver.find_element(By.XPATH, "//input[@data-test='login-button']")
    login_button.click()
    WebDriverWait(driver, 10).until(EC.url_to_be("https://www.saucedemo.com/inventory.html"))
    time.sleep(3)

    # Add an item to the cart
    add_to_cart_button = driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']")
    add_to_cart_button.click()
    time.sleep(3)

    # Check the cart count
    cart_count = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='shopping_cart_badge']")))
    time.sleep(3)
    
    expected_count = "1"
    actual_count = cart_count.text

    # Assert the cart count
    if compare_sentences(expected_count, actual_count):
        sys.exit(0)
    else:
        sys.exit(1)

except Exception as e:
    print("An error occurred during the test execution:", e)
    sys.exit(1)

finally:
    driver.quit()
