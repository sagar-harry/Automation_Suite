
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from compare_sentences import compare_sentences

def test_successful_login():
    # Setting up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")

    # Initialize the WebDriver
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Maximize the browser
        driver.maximize_window()

        # Navigate to the login page
        driver.get("https://saucedemo.com/")

        # Wait for 3 seconds before every action
        time.sleep(3)

        # Locate the username field and enter username
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@data-test='username']"))
        )
        username_field.send_keys("standard_user")

        time.sleep(3)

        # Locate the password field and enter password
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@data-test='password']"))
        )
        password_field.send_keys("secret_sauce")

        time.sleep(3)

        # Locate the login button and click it
        login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@data-test='login-button']"))
        )
        login_button.click()

        time.sleep(3)

        # Verify redirection to the products page
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://saucedemo.com/inventory.html")
        )

        # Locate the page title and verify
        page_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@data-test='title']"))
        )
        assert compare_sentences(page_title.text, "Products"), "Title does not match"

        # Verify the presence of Shopping Cart icon
        shopping_cart_icon = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@data-test='shopping-cart-link']"))
        )
        assert shopping_cart_icon is not None, "Shopping Cart Icon not found"

        # Verify the presence of Menu button
        menu_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@id='react-burger-menu-btn']"))
        )
        assert menu_button is not None, "Menu Button not found"

        print("Test passed")
        sys.exit(0)

    except Exception as e:
        print(f"Test failed: {e}")
        sys.exit(1)

    finally:
        # Close the driver
        driver.quit()

if __name__ == "__main__":
    test_successful_login()
