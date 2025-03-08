
import time
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from compare_sentences import compare_sentences

def test_sauce_demo_login():
    try:
        # Configure Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-popup-blocking")

        # Initialize WebDriver
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)

        # Step 1: Navigate to SauceDemo login page
        driver.get("https://www.saucedemo.com/")
        time.sleep(3)

        # Step 2: Enter username "standard_user"
        username_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@data-test='username']")))
        username_input.send_keys("standard_user")
        time.sleep(3)

        # Step 3: Enter password "secret_sauce"
        password_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@data-test='password']")))
        password_input.send_keys("secret_sauce")
        time.sleep(3)

        # Step 4: Click the "Login" button
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@data-test='login-button']")))
        login_button.click()
        time.sleep(3)

        # Step 5: Verify redirection to product listing page
        expected_url = "https://www.saucedemo.com/inventory.html"
        wait.until(EC.url_to_be(expected_url))

        # Step 6: Verify product list is visible
        product_page_title = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='title' and text()='Products']")))
        actual_title = product_page_title.text
        assert compare_sentences(actual_title, "Products"), "Page title does not match"

        product_list_container = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-test='inventory-list']")))
        assert product_list_container.is_displayed(), "Product list is not displayed"

        # Test passed
        sys.exit(0)
    
    except Exception as e:
        print(f"Test failed due to: {e}")
        sys.exit(1)
    
    finally:
        driver.quit()

if __name__ == "__main__":
    test_sauce_demo_login()
