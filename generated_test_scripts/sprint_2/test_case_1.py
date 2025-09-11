
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import sys

chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-features=NetworkService")
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("https://saucedemo.com/")
    time.sleep(5)

    # Wait for the login page to load
    driver.implicitly_wait(5)

    # Login
    driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@id='login-button']").click()
    time.sleep(3)

    # Add Bike Light to the cart
    driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']").click()
    time.sleep(3)

    # Add Fleece Jacket to the cart
    driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']").click()
    time.sleep(3)

    # Click on the cart icon
    driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
    time.sleep(3)

    # Proceed to checkout
    driver.find_element(By.XPATH, "//button[@id='checkout']").click()
    time.sleep(3)

    # Enter user information
    driver.find_element(By.XPATH, "//input[@id='first-name']").send_keys("Jonnathan")
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@id='last-name']").send_keys("K")
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@id='postal-code']").send_keys("10007")
    time.sleep(3)

    # Continue to complete the purchase
    driver.find_element(By.XPATH, "//input[@id='continue']").click()
    time.sleep(3)

    # Finish the purchase
    driver.find_element(By.XPATH, "//button[@id='finish']").click()
    time.sleep(3)

    # Save snapshot
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\purchase.png")
    
    # Return to homepage
    driver.find_element(By.XPATH, "//button[@id='back-to-products']").click()
    time.sleep(3)
    
    # Logout
    driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//a[@id='logout_sidebar_link']").click()
    time.sleep(3)

    driver.quit()
    sys.exit(0)

except Exception as e:
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\error.png")
    driver.quit()
    sys.exit(1)
