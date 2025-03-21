
import time
import sys
import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        
    def login(self, username, password):
        self.driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

try:
    # Set up ChromeOptions
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-features=NetworkService")
    
    # Initialize WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    
    # Open the webpage
    driver.get("https://saucedemo.com/")
    time.sleep(5)
    
    # Maximize browser window
    driver.maximize_window()

    # Perform login
    login_page = LoginPage(driver)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]')))
    login_page.login("standard_user", "secret_sauce")
    time.sleep(3)
    
    # Add Bike Light and Fleece Jacket to the cart
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
    time.sleep(3)
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]')))
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]').click()
    time.sleep(3)

    # Verify the cart badge displays '2'
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
    cart_count = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text
    assert cart_count == '2', "Cart count mismatch after add: expected '2' but got '{0}'".format(cart_count)
    
    # Remove both items
    driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]').click()
    time.sleep(3)
    
    driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]').click()
    time.sleep(3)

    # Verify the cart badge does not exist
    try:
        driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        assert False, "Cart badge still exists when it should not"
    except:
        pass

    # Add Bolt T-Shirt to the cart
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')))
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    time.sleep(3)

    # Verify the cart badge displays '1'
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
    cart_count = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text
    assert cart_count == '1', "Cart count mismatch after add: expected '1' but got '{0}'".format(cart_count)

    # Take a snapshot
    driver.save_screenshot(r'C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png')

    # Close the browser
    driver.quit()

    # Successfully pass test
    sys.exit(0)

except Exception as e:
    # Print stack trace for debugging
    traceback.print_exc()
    # Take a snapshot
    driver.save_screenshot(r'C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png')
    # Close the browser
    driver.quit()
    # Exit with error
    sys.exit(1)
