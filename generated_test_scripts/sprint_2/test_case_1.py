
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-features=NetworkService")

    # Launch browser
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    
    # Navigate to the website
    driver.get("https://saucedemo.com/")
    time.sleep(5)

    # Login
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]'))).send_keys("standard_user")
    time.sleep(3)
    
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
    time.sleep(3)
    
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(3)

    # Add items to cart
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
    time.sleep(3)
    
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    time.sleep(3)

    # Go to cart
    driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
    time.sleep(3)

    # Checkout
    driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
    time.sleep(3)
    
    # Enter checkout information
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="first-name"]'))).send_keys("somename")
    time.sleep(3)
    
    driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("lastname")
    time.sleep(3)
    
    driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("123456")
    time.sleep(3)
    
    driver.find_element(By.XPATH, '//*[@id="continue"]').click()
    time.sleep(3)

    # Finish purchase
    driver.find_element(By.XPATH, '//*[@id="finish"]').click()
    time.sleep(3)

    # Back to homepage
    driver.find_element(By.XPATH, '//*[@id="back-to-products"]').click()
    time.sleep(3)

    # Logout
    driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
    time.sleep(3)
    
    driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]').click()
    time.sleep(3)

    # Capture screenshot
    driver.save_screenshot('C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\checkout_screen.png')
    
    # Exit successfully
    sys.exit(0)

except Exception as e:
    print(f"Test Failed: {e}")
    sys.exit(1)

finally:
    # Close browser
    driver.quit()
