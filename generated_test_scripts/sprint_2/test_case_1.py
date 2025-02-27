
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def test_login_logout_flow():
    try:
        # Setup Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-features=NetworkService")

        # Initialize WebDriver
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.implicitly_wait(10)  # Implicit wait

        # Open the website
        driver.get("https://saucedemo.com/")
        time.sleep(5)  # Wait for 5 secs after opening the page
        
        wait = WebDriverWait(driver, 10)  # Explicit wait

        # Login
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]'))).send_keys("standard_user")
        time.sleep(3)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]'))).send_keys("secret_sauce")
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]'))).click()
        time.sleep(3)
        
        # Add items to cart
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))).click()
        time.sleep(3)
        
        # Go to cart
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="shopping_cart_container"]/a'))).click()
        time.sleep(3)
        
        # Proceed to checkout
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkout"]'))).click()
        time.sleep(3)
        
        # Enter checkout information
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="first-name"]'))).send_keys("somename")
        time.sleep(3)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="last-name"]'))).send_keys("lastname")
        time.sleep(3)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="postal-code"]'))).send_keys("123456")
        time.sleep(3)
        
        # Continue and finish purchase
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="continue"]'))).click()
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="finish"]'))).click()
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="back-to-products"]')))
        time.sleep(3)
        
        # Logout
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-burger-menu-btn"]'))).click()
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="logout_sidebar_link"]'))).click()
        time.sleep(3)

        # Save screenshot
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\final_state.png")
        
        # Test passed
        sys.exit(0)

    except Exception as e:
        print(f"Test failed: {str(e)}")
        sys.exit(1)

    finally:
        driver.quit()

test_login_logout_flow()
