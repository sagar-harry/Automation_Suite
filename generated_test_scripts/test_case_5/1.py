
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from compare_sentences import compare_sentences

def run_test():
    # Disable notifications, pop-ups and run in incognito mode
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Open the SauceDemo website
        driver.get("https://saucedemo.com/")
        time.sleep(3)

        # Find the username input field by ID 'user-name' and enter 'standard_user'
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='user-name']"))
        )
        time.sleep(3)
        username_field.send_keys('standard_user')

        # Find the password input field by ID 'password' and enter 'secret_sauce'
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='password']"))
        )
        time.sleep(3)
        password_field.send_keys('secret_sauce')

        # Find the login button by data-test attribute 'login-button' and click it
        login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@data-test='login-button']"))
        )
        time.sleep(3)
        login_button.click()

        # Verify redirection to the Product Listing Page with URL '/inventory.html'
        WebDriverWait(driver, 10).until(
            EC.url_contains('/inventory.html')
        )
        time.sleep(3)

        # Add a product to the cart
        add_to_cart_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']"))
        )
        time.sleep(3)
        add_to_cart_button.click()

        # Proceed to checkout by filling user info and reaching the Overview page
        proceed_to_checkout_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@data-test='checkout']"))
        )
        time.sleep(3)
        proceed_to_checkout_button.click()

        first_name_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='first-name']"))
        )
        time.sleep(3)
        first_name_field.send_keys('John')

        last_name_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='last-name']"))
        )
        time.sleep(3)
        last_name_field.send_keys('Doe')

        postal_code_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='postal-code']"))
        )
        time.sleep(3)
        postal_code_field.send_keys('12345')

        continue_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@data-test='continue']"))
        )
        time.sleep(3)
        continue_button.click()

        # Click 'Finish' button on the checkout overview page
        finish_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@data-test='finish']"))
        )
        time.sleep(3)
        finish_button.click()

        # Verify redirection to Order Confirmation Page with URL '/checkout-complete.html'
        WebDriverWait(driver, 10).until(
            EC.url_contains('/checkout-complete.html')
        )
        time.sleep(3)

        # Verify presence of confirmation message
        confirmation_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h2[@data-test='complete-header' and text()='Thank you for your order!']"))
        )
        time.sleep(3)
        assert compare_sentences(confirmation_message.text, 'Thank you for your order!')

        sys.exit(0)

    except Exception as e:
        print(f"Test failed: {e}")
        sys.exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    run_test()
