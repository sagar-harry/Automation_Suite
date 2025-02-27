
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define URL, credentials, and locators
URL = "https://saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"
locators = {
    "username": '//*[@id="user-name"]',
    "password": '//*[@id="password"]',
    "login_button": '//*[@id="login-button"]',
    "bike_light": '//*[@id="add-to-cart-sauce-labs-bike-light"]',
    "fleece_jacket": '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]',
    "cart_count": '//*[@id="shopping_cart_container"]/a/span'
}

# Chrome options
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-features=NetworkService")
chrome_options.add_argument("start-maximized")

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Open the website
    driver.get(URL)
    time.sleep(5)  # Wait for the page to load

    # Login to the site
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, locators["username"])))
    driver.find_element(By.XPATH, locators["username"]).send_keys(USERNAME)
    time.sleep(3)  # Wait before the next action
    driver.find_element(By.XPATH, locators["password"]).send_keys(PASSWORD)
    time.sleep(3)  # Wait before the next action
    driver.find_element(By.XPATH, locators["login_button"]).click()
    
    # Wait for and add Bike Light to the cart
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, locators["bike_light"])))
    driver.find_element(By.XPATH, locators["bike_light"]).click()
    time.sleep(3)  # Wait before the next action

    # Wait for and add Fleece Jacket to the cart
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, locators["fleece_jacket"])))
    driver.find_element(By.XPATH, locators["fleece_jacket"]).click()
    time.sleep(3)  # Wait before the next action

    # Verify cart count
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, locators["cart_count"])))
    cart_count = driver.find_element(By.XPATH, locators["cart_count"]).text

    if cart_count == '2':
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\cart_test_passed.png")
        sys.exit(0)
    else:
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\cart_test_failed.png")
        sys.exit(1)

except Exception as e:
    driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\exception_occurred.png")
    sys.exit(1)
finally:
    # Clean-up actions
    driver.quit()
