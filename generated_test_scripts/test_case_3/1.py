
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from compare_sentences import compare_sentences

def main():
    try:
        # Set up Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--incognito")

        # Initialize the WebDriver
        driver = webdriver.Chrome(options=chrome_options)

        # Maximize the window
        driver.maximize_window()

        # Navigate to the login page
        driver.get('https://saucedemo.com')

        # Wait for the page to load
        time.sleep(3)
        
        # Log in to the application
        driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='login-button']").click()

        # Wait and assert the redirection to the product listing page
        WebDriverWait(driver, 10).until(EC.url_contains("inventory"))
        time.sleep(3)

        # Add "Sauce Labs Backpack" to the cart
        driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']").click()
        time.sleep(3)

        # Navigate to the shopping cart page
        driver.find_element(By.XPATH, "//a[@data-test='shopping-cart-link']").click()
        time.sleep(3)

        # Click on the "Checkout" button
        driver.find_element(By.XPATH, "//button[@id='checkout']").click()

        # Wait and assert the redirection to the checkout step-1 page
        WebDriverWait(driver, 10).until(EC.url_contains("checkout-step-one"))
        time.sleep(3)

        # Fill in the checkout information
        driver.find_element(By.XPATH, "//input[@id='first-name']").send_keys("John")
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='last-name']").send_keys("Doe")
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='postal-code']").send_keys("12345")
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='continue']").click()

        # Wait and assert the redirection to the checkout step-2 page
        WebDriverWait(driver, 10).until(EC.url_contains("checkout-step-two"))
        time.sleep(3)

        # Complete the purchase
        driver.find_element(By.XPATH, "//button[@id='finish']").click()

        # Wait and assert the order confirmation
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h2[@data-test='complete-header' and text()='Thank you for your order!']")))
        
        # Validate the order confirmation message
        confirmation_message = driver.find_element(By.XPATH,"//h2[@data-test='complete-header' and text()='Thank you for your order!']").text
        assert compare_sentences(confirmation_message, "Thank you for your order!"), "Order confirmation message mismatch!"
        
        # Exit successfully
        sys.exit(0)

    except Exception as e:
        print(f"Test failed due to: {e}")
        sys.exit(1)
    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    main()
