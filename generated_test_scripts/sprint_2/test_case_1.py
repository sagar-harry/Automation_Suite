
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-features=NetworkService")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://saucedemo.com/")
time.sleep(5)
driver.maximize_window()

wait = WebDriverWait(driver, 10)

try:
    # Login
    username = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]')))
    password = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]')))
    login_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="login-button"]')))

    username.send_keys("standard_user")
    time.sleep(3)
    password.send_keys("secret_sauce")
    time.sleep(3)
    login_button.click()
    time.sleep(3)

    # Add items to cart
    bike_light = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
    fleece_jacket = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')))
    
    bike_light.click()
    time.sleep(3)
    fleece_jacket.click()
    time.sleep(3)

    # Navigate to cart
    cart_icon = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a')))
    
    cart_icon.click()
    time.sleep(3)

    # Proceed to checkout
    checkout_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="checkout"]')))
    
    checkout_button.click()
    time.sleep(3)

    # Enter checkout information
    first_name = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="first-name"]')))
    last_name = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="last-name"]')))
    postal_code = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="postal-code"]')))
    continue_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="continue"]')))
    
    first_name.send_keys("somename")
    time.sleep(3)
    last_name.send_keys("lastname")
    time.sleep(3)
    postal_code.send_keys("123456")
    time.sleep(3)
    continue_button.click()
    time.sleep(3)

    # Complete purchase
    finish_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="finish"]')))
    
    finish_button.click()
    time.sleep(3)

    # Navigate back to homepage
    back_to_products = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="back-to-products"]')))
    
    back_to_products.click()
    time.sleep(3)

    # Logout
    logout_sidebar = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-burger-menu-btn"]')))
    
    logout_sidebar.click()
    time.sleep(3)

    logout_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="logout_sidebar_link"]')))
    
    logout_button.click()
    time.sleep(3)

    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")
    
    sys.exit(0)
except Exception as e:
    print(f"Test failed: {str(e)}")
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\error_screenshot.png")
    sys.exit(1)
finally:
    driver.quit()
