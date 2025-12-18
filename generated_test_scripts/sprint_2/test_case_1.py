
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import sys

options = Options()
options.add_argument("--incognito")
options.add_argument("--disable-notifications")
options.add_argument("--disable-features=NetworkService")
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

try:
    # Open the website
    driver.get("https://saucedemo.com/")
    time.sleep(5)

    # Log in to the application
    driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@id='login-button']").click()
    time.sleep(3)
    
    # Add items to the cart
    driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']").click()
    time.sleep(3)
    
    # Go to cart
    driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
    time.sleep(3)
    
    # Proceed to checkout
    driver.find_element(By.XPATH, "//button[@id='checkout']").click()
    time.sleep(3)
    
    # Fill in checkout information
    driver.find_element(By.XPATH, "//input[@id='first-name']").send_keys("Jonnathan")
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@id='last-name']").send_keys("K")
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@id='postal-code']").send_keys("10007")
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@id='continue']").click()
    time.sleep(3)
    
    # Complete purchase
    driver.find_element(By.XPATH, "//button[@id='finish']").click()
    time.sleep(3)
    
    # Return to home
    driver.find_element(By.XPATH, "//button[@id='back-to-products']").click()
    time.sleep(3)
    
    # Log out of application
    driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//a[@id='logout_sidebar_link']").click()
    time.sleep(3)

    # Save a snapshot before closing
    driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot.png")
    
    # Exit successfully
    sys.exit(0)

except Exception as e:
    # Save a snapshot before closing
    driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot.png")
    sys.exit(1)

finally:
    driver.quit()
