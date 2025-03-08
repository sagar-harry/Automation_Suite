
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from compare_sentences import compare_sentences

def run_test_case():
    # Setting up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--incognito")
    
    try:
        # Initialize the WebDriver
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        
        # Open the login page
        driver.get("https://www.saucedemo.com/")
        
        # Wait for 3 seconds
        time.sleep(3)
        
        # Wait for the username input to be present and enter the username
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='user-name']"))
        )
        username_input = driver.find_element(By.XPATH, "//input[@id='user-name']")
        username_input.send_keys("standard_user")
        
        # Wait for the password input to be present and enter the password
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='password']"))
        )
        password_input = driver.find_element(By.XPATH, "//input[@id='password']")
        password_input.send_keys("secret_sauce")
        
        # Wait for the login button and click it
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='login-button']"))
        )
        login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
        login_button.click()
        
        # Wait for 3 seconds
        time.sleep(3)
        
        # Wait for the add-to-cart button for Sauce Labs Backpack and click it
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']"))
        )
        add_to_cart_button = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
        add_to_cart_button.click()
        
        # Wait for 3 seconds
        time.sleep(3)
        
        # Wait for the cart icon to be visible
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='shopping_cart_container']//a[@class='shopping_cart_link']"))
        )
        cart_icon = driver.find_element(By.XPATH, "//div[@id='shopping_cart_container']//a[@class='shopping_cart_link']")
        cart_count_text = cart_icon.text
        
        # Validate cart count
        if compare_sentences(cart_count_text.strip(), "1"):
            print("Test Passed: Cart count is as expected.")
            sys.exit(0)
        else:
            print("Test Failed: Cart count is not as expected.")
            sys.exit(1)
    
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
    
    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    run_test_case()
