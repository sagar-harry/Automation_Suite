
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time
from compare_sentences import compare_sentences

def validate_successful_login():
    # Initialize Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")

    # Start the browser
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Maximize the browser window
        driver.maximize_window()

        # Given: The user is on the SauceDemo login page
        driver.get("https://saucedemo.com/")
        time.sleep(3)  # Explicit wait for 3 seconds

        # When: The user enters valid username and password
        wait = WebDriverWait(driver, 10)
        username_field = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='user-name']")))
        password_field = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='password']")))
        login_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='login-button']")))

        username_field.send_keys("standard_user")
        time.sleep(3)  # Explicit wait for 3 seconds
        password_field.send_keys("secret_sauce")
        time.sleep(3)  # Explicit wait for 3 seconds

        # And: The user clicks on the login button
        login_button.click()
        time.sleep(3)  # Explicit wait for 3 seconds

        # Then: The user should be redirected to the Product Listing Page
        wait.until(EC.url_contains("/inventory.html"))
        current_url = driver.current_url
        expected_url = "https://saucedemo.com/inventory.html"

        # Assert URL and text
        if compare_sentences(current_url, expected_url):
            product_listing_title = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@data-test='title']")))
            if compare_sentences(product_listing_title.text, "Products"):
                print("Test Case Passed")
                sys.exit(0)
            else:
                print("Test Case Failed: Title mismatch")
                sys.exit(1)
        else:
            print("Test Case Failed: URL mismatch")
            sys.exit(1)

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    validate_successful_login()
