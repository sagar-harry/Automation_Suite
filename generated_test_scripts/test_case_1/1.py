
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time
from compare_sentences import compare_sentences

# Function to validate the login process on SauceDemo
def validate_successful_login():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")

    driver = webdriver.Chrome(options=options)
    
    try:
        # Open the SauceDemo login page
        driver.get("https://saucedemo.com/")
        driver.maximize_window()

        # Wait for the username input and set the username
        time.sleep(3)
        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@data-test='username']"))
        )
        username_input.send_keys("standard_user")

        # Wait for the password input and set the password
        time.sleep(3)
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@data-test='password']"))
        )
        password_input.send_keys("secret_sauce")

        # Wait for the login button and click it
        time.sleep(3)
        login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@data-test='login-button']"))
        )
        login_button.click()

        # Wait for the product listing page to load
        time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://saucedemo.com/inventory.html")
        )

        # Validate the page title
        time.sleep(3)
        product_page_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@data-test='title' and text()='Products']"))
        )
        if not compare_sentences(product_page_title.text, "Products"):
            sys.exit(1)

        # Validate the cart icon in the header
        time.sleep(3)
        cart_icon = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@data-test='shopping-cart-link']"))
        )
        if not cart_icon.is_displayed():
            sys.exit(1)
        
        sys.exit(0)

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    validate_successful_login()
