
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import sys
from compare_sentences import compare_sentences

def main():
    url = "https://www.saucedemo.com"
    expected_product_page_title = "Products"
    expected_checkout_info_page_title = "Checkout: Your Information"
    
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--incognito")

    # Initialize webdriver
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get(url)

    try:
        # Wait for page load
        sleep(3)

        # Step 1: Login
        driver.find_element(By.XPATH, "//input[@data-test='username']").send_keys("standard_user")
        sleep(3)
        driver.find_element(By.XPATH, "//input[@data-test='password']").send_keys("secret_sauce")
        sleep(3)
        driver.find_element(By.XPATH, "//input[@data-test='login-button']").click()
        sleep(3)

        # Verify redirection to product listing page
        current_page_title = driver.find_element(By.XPATH, "//span[@data-test='title']").text
        assert compare_sentences(current_page_title, expected_product_page_title)

        # Step 2: Add product to cart
        driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']").click()
        sleep(3)

        # Navigate to shopping cart
        driver.find_element(By.XPATH, "//a[@data-test='shopping-cart-link']").click()
        sleep(3)

        # Click Checkout
        driver.find_element(By.XPATH, "//button[@data-test='checkout']").click()
        sleep(3)

        # Verify redirection to Checkout Step 1: User Info Page
        current_checkout_title = driver.find_element(By.XPATH, "//span[@data-test='title']").text
        assert compare_sentences(current_checkout_title, expected_checkout_info_page_title)

        # Step 3: Fill user info
        driver.find_element(By.XPATH, "//input[@data-test='firstName']").send_keys("John")
        sleep(3)
        driver.find_element(By.XPATH, "//input[@data-test='lastName']").send_keys("Doe")
        sleep(3)
        driver.find_element(By.XPATH, "//input[@data-test='postalCode']").send_keys("12345")
        sleep(3)

        print("Test case passed.")
        sys.exit(0)

    except Exception as e:
        print(f"Test case failed: {e}")
        sys.exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
