
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Chrome options
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--disable-features=NetworkService")

try:
    # Setup WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    
    # Maximize window and open the website
    driver.maximize_window()
    driver.get("https://saucedemo.com/")
    time.sleep(5)

    # Wait for the login elements
    wait = WebDriverWait(driver, 10)
    user_name = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]')))
    password = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]')))
    login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')
    
    # Login to the application
    user_name.send_keys("standard_user")
    time.sleep(3)
    password.send_keys("secret_sauce")
    time.sleep(3)
    login_button.click()

    # Add 'Bike Light' and 'Fleece Jacket' to the cart
    bike_light = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
    fleece_jacket = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')))
    bike_light.click()
    time.sleep(3)
    fleece_jacket.click()
    time.sleep(3)
    
    # Proceed to checkout
    cart_icon = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a')))
    cart_icon.click()
    time.sleep(3)
    
    checkout = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout"]')))
    checkout.click()
    time.sleep(3)

    # Enter checkout information
    first_name = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="first-name"]')))
    last_name = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="last-name"]')))
    postal_code = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="postal-code"]')))
    
    first_name.send_keys("Jonnathan")
    time.sleep(3)
    last_name.send_keys("K")
    time.sleep(3)
    postal_code.send_keys("10007")
    time.sleep(3)

    # Complete the purchase
    continue_button = driver.find_element(By.XPATH, '//*[@id="continue"]')
    continue_button.click()
    time.sleep(3)
    
    finish_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="finish"]')))
    finish_button.click()
    time.sleep(3)

    # Return to home page
    back_to_products = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="back-to-products"]')))
    back_to_products.click()
    time.sleep(3)

    # Logout from the application
    logout_sidebar = driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]')
    logout_sidebar.click()
    time.sleep(3)

    logout_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="logout_sidebar_link"]')))
    logout_button.click()
    time.sleep(3)

    # Save snapshot of the page
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")

    sys.exit(0)

except Exception as e:
    print(f"Test failed due to {e}")
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\error_screenshot.png")
    sys.exit(1)

finally:
    driver.quit()
