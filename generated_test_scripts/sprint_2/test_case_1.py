
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure ChromeOptions
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-notifications')
options.add_argument('--incognito')
options.add_argument('--disable-popup-blocking')
options.add_argument('--disable-features=NetworkService')
options.add_argument('--start-maximized')

# Initialize driver
driver = webdriver.Chrome(options=options)

try:
    # Navigating to the URL
    driver.get("https://saucedemo.com/")
    time.sleep(5)

    # Login
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys('standard_user')
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(5)

    # Add items to the cart
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    time.sleep(3)

    # Go to the cart and proceed to checkout
    driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
    time.sleep(3)

    # Enter checkout information
    driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys('somename')
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys('lastname')
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys('123456')
    time.sleep(3)

    # Continue and complete purchase
    driver.find_element(By.XPATH, '//*[@id="continue"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="finish"]').click()
    time.sleep(3)

    # Return to homepage
    driver.find_element(By.XPATH, '//*[@id="back-to-products"]').click()
    time.sleep(3)

    # Logout
    driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
    time.sleep(3)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="logout_sidebar_link"]'))
    ).click()
    time.sleep(3)

    print("Test Case Passed")
    sys.exit(0)
except Exception as e:
    print(f"Test Case Failed due to {e}")
    sys.exit(1)
finally:
    driver.quit()
