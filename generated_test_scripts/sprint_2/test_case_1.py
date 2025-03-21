
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import sys

def test_purchase_flow():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-features=NetworkService")
    
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        driver.maximize_window()
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        
        # Login
        username = driver.find_element(By.XPATH, '//*[@id="user-name"]')
        password = driver.find_element(By.XPATH, '//*[@id="password"]')
        login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')
        
        username.send_keys("standard_user")
        time.sleep(3)
        password.send_keys("secret_sauce")
        time.sleep(3)
        login_button.click()
        time.sleep(3)
        
        # Add items to cart
        bike_light = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
        fleece_jacket = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        
        bike_light.click()
        time.sleep(3)
        fleece_jacket.click()
        time.sleep(3)
        
        # Proceed to checkout
        cart_icon = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
        cart_icon.click()
        time.sleep(3)
        
        checkout = driver.find_element(By.XPATH, '//*[@id="checkout"]')
        checkout.click()
        time.sleep(3)
        
        # Enter checkout information
        first_name = driver.find_element(By.XPATH, '//*[@id="first-name"]')
        last_name = driver.find_element(By.XPATH, '//*[@id="last-name"]')
        postal_code = driver.find_element(By.XPATH, '//*[@id="postal-code"]')
        
        first_name.send_keys("Jonnathan")
        time.sleep(3)
        last_name.send_keys("K")
        time.sleep(3)
        postal_code.send_keys("10007")
        time.sleep(3)
        
        continue_button = driver.find_element(By.XPATH, '//*[@id="continue"]')
        continue_button.click()
        time.sleep(3)
        
        # Complete the purchase
        finish_button = driver.find_element(By.XPATH, '//*[@id="finish"]')
        finish_button.click()
        time.sleep(3)
        
        # Return to homepage
        back_to_products = driver.find_element(By.XPATH, '//*[@id="back-to-products"]')
        back_to_products.click()
        time.sleep(3)
        
        # Logout
        logout_sidebar = driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]')
        logout_sidebar.click()
        time.sleep(3)
        
        logout_button = driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]')
        logout_button.click()
        time.sleep(3)
        
        # Save a screenshot of the result
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")
        
        sys.exit(0)
    except Exception as e:
        print("Test failed:", e)
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\error_screenshot.png")
        sys.exit(1)
    finally:
        driver.quit()

test_purchase_flow()
