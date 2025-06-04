
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import sys
import os

# Configure Selenium WebDriver
options = Options()
options.add_argument("--incognito")
options.add_argument("--disable-notifications")
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-features=NetworkService")

# Initialize WebDriver
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(10)

try:
    driver.get("https://saucedemo.com/")
    time.sleep(5)

    # Login
    driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@id='login-button']").click()
    time.sleep(3)

    # Add 'Bike Light' and 'Fleece Jacket' to cart
    driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']").click()
    time.sleep(3)

    # Proceed to Checkout
    driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[@id='checkout']").click()
    time.sleep(3)

    # Enter checkout information
    driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Jonnathan")
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("K")
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@placeholder='Zip/Postal Code']").send_keys("10007")
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@id='continue']").click()
    time.sleep(3)

    # Finish and return to homepage
    driver.find_element(By.XPATH, "//button[@id='finish']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[@id='back-to-products']").click()
    time.sleep(3)

    # Log out
    driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//a[@id='logout_sidebar_link']").click()
    time.sleep(3)

    # Save screenshot
    if not os.path.exists("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots"):
        os.makedirs("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots")

    driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot.png")

    sys.exit(0)

except Exception as e:
    print(f"An error occurred: {e}")
    driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\error_screenshot.png")
    sys.exit(1)

finally:
    driver.quit()
