
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import sys
import time
from compare_sentences import compare_sentences

def test_cart_count():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    
    # Initialize WebDriver
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    
    try:
        # Maximize the page
        driver.maximize_window()
        
        # Navigate to the SauceDemo login page
        driver.get("https://saucedemo.com/")
        
        # Wait for 3 secs before every action
        time.sleep(3)

        # Wait for Username Field to be present and enter username
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='user-name']"))
        )
        username_field.send_keys("standard_user")

        # Wait for 3 secs before every action
        time.sleep(3)

        # Wait for Password Field to be present and enter password
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='password']"))
        )
        password_field.send_keys("secret_sauce")

        # Wait for 3 secs before every action
        time.sleep(3)

        # Wait for Login Button to be clickable and click it
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='login-button']"))
        )
        login_button.click()

        # Wait for 3 secs before every action
        time.sleep(3)

        # Verify user is redirected to the Product Listing Page
        current_url = driver.current_url
        if not compare_sentences(current_url, "https://www.saucedemo.com/inventory.html"):
            print("Failed: User was not redirected to Product Listing Page")
            sys.exit(1)

        # Wait for Add to Cart Button for Product 1 to be clickable and click it
        add_to_cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']"))
        )
        add_to_cart_button.click()

        # Wait for 3 secs before every action
        time.sleep(3)

        # Wait for Cart Badge to appear and verify the count
        cart_badge = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='shopping_cart_container']//a[@class='shopping_cart_link']/span"))
        )
        cart_count = cart_badge.text
        if not compare_sentences(cart_count, "1"):
            print("Failed: Cart count is not as expected")
            sys.exit(1)

        print("Passed: Cart count is as expected")
        sys.exit(0)

    except Exception as e:
        print(f"Test Failed: {e}")
        sys.exit(1)

    finally:
        driver.quit()

test_cart_count()
