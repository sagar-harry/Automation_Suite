
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from compare_sentences import compare_sentences

def test_login_and_product_listing():
    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--start-maximized")

    # Initialize the driver
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Step 1: Open the SauceDemo website
        driver.get("https://saucedemo.com/")
        time.sleep(3)

        # Step 2: Find the username input field and enter 'standard_user'
        username_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='user-name']"))
        )
        username_input.send_keys("standard_user")
        time.sleep(3)

        # Step 3: Find the password input field and enter 'secret_sauce'
        password_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='password']"))
        )
        password_input.send_keys("secret_sauce")
        time.sleep(3)

        # Step 4: Find the login button and click it
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@data-test='login-button']"))
        )
        login_button.click()
        time.sleep(3)

        # Step 5: Verify redirection to the Product Listing Page
        WebDriverWait(driver, 10).until(
            EC.url_contains("/inventory.html")
        )
        assert compare_sentences(driver.current_url, driver.current_url.split("?")[0] + "/inventory.html")
        time.sleep(3)

        # Step 6: Check the presence of products in the listing
        products_in_listing = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//*[@class='inventory_item']"))
        )
        assert len(products_in_listing) > 0

        print("Test case passed.")
        sys.exit(0)

    except Exception as e:
        print(f"Test case failed: {e}")
        sys.exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    test_login_and_product_listing()
