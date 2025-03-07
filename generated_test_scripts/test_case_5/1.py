
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from compare_sentences import compare_sentences

def main():
    chrome_options = Options()
    # Disable notifications, pop-ups and run in incognito mode
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_argument('--disable-popup-blocking')
    chrome_options.add_argument('--incognito')

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    try:
        # Step 1: Navigate to the SauceDemo login page
        driver.get('https://saucedemo.com')
        time.sleep(3)

        # Step 2: Enter Login Credentials
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='user-name']"))).send_keys('standard_user')
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='password']"))).send_keys('secret_sauce')
        time.sleep(3)

        # Step 3: Click the login button
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='login-button']"))).click()
        time.sleep(3)

        # Step 4: Verify User is redirected to the product listing page
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Products')]")))

        # Step 5: Add 'Sauce Labs Backpack' to the cart
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']"))).click()
        time.sleep(3)

        # Step 6: Navigate to the shopping cart
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='shopping_cart_link']"))).click()
        time.sleep(3)

        # Step 7: Click the Checkout button
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='checkout']"))).click()
        time.sleep(3)

        # Step 8: Fill in user info and continue
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='first-name']"))).send_keys('John')
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='last-name']"))).send_keys('Doe')
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='postal-code']"))).send_keys('12345')
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='continue']"))).click()
        time.sleep(3)

        # Step 9: Click the Finish button
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='finish']"))).click()
        time.sleep(3)

        # Step 10: Verify order confirmation
        confirmation_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//h2[text()='Thank you for your order!']")))
        if compare_sentences(confirmation_message.text, 'Thank you for your order!'):
            print("Test Passed")
            sys.exit(0)
        else:
            print("Test Failed")
            sys.exit(1)
        
    except Exception as e:
        print(f"Test Failed: {e}")
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
