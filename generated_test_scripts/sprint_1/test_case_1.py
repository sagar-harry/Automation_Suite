
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def take_screenshot(driver):
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")

try:
    # Chrome options configuration
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-features=NetworkService")

    # Setup the driver
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(5)

    # Navigate to the website
    driver.get("https://saucedemo.com/")
    time.sleep(5)

    # Logging in
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

    # Adding items to the cart
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]').click()
    time.sleep(3)

    # Verify cart badge display '2'
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'), '2'))

    # Remove items
    driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]').click()
    time.sleep(3)

    # Verify cart count element doesn't exist
    assert not driver.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')

    # Add Bolt T-Shirt to the cart
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    time.sleep(3)

    # Verify cart badge display '1'
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'), '1'))

    # Take a screenshot before closing
    take_screenshot(driver)

    # Test case passed
    sys.exit(0)

except Exception as e:
    take_screenshot(driver)
    print(str(e))
    sys.exit(1)
finally:
    driver.quit()
