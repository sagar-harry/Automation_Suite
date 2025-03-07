
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from time import sleep
from compare_sentences import compare_sentences
import sys

def main():
    # Chrome options setup
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")

    # Initialize driver
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 10)

    try:
        # Navigate to the home page
        driver.get("https://www.saucedemo.com")
        
        # Step 1: Ensure Sauce Labs Backpack is in the cart
        driver.get("https://www.saucedemo.com/cart.html")
        sleep(3) # Wait for cart page to load
        wait.until(EC.presence_of_element_located((By.XPATH, "//*[@data-test='inventory-item-name' and text()='Sauce Labs Backpack']")))

        # Step 2: Navigate to checkout Step 1 page
        checkout_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@data-test='checkout']")))
        checkout_button.click()
        sleep(3)

        # Step 3: Fill in user information
        first_name_input = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='first-name']")))
        last_name_input = driver.find_element(By.XPATH, "//*[@id='last-name']")
        postal_code_input = driver.find_element(By.XPATH, "//*[@id='postal-code']")

        first_name_input.send_keys("John")
        last_name_input.send_keys("Doe")
        postal_code_input.send_keys("90210")

        # Step 4: Click continue to proceed to checkout overview
        continue_button = driver.find_element(By.XPATH, "//*[@data-test='continue']")
        continue_button.click()
        sleep(3)

        # Step 5: Finalize checkout by clicking finish
        finish_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@data-test='finish']")))
        finish_button.click()
        sleep(3)

        # Step 6: Verify order confirmation message
        confirmation_message = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@data-test='complete-header' and text()='Thank you for your order!']")))

        assert compare_sentences(confirmation_message.text, "Thank you for your order!") == 0
        sys.exit(0)

    except (TimeoutException, NoSuchElementException) as e:
        print(f"Test Failed: {e}")
        sys.exit(1)
    
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
