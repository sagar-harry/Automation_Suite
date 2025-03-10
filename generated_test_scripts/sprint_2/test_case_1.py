
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

try:
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popups")
    options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    driver.get("https://saucedemo.com/")
    time.sleep(5)

    wait = WebDriverWait(driver, 10)

    # Login
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]'))).send_keys('standard_user')
    time.sleep(3)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]'))).send_keys('secret_sauce')
    time.sleep(3)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]'))).click()
    time.sleep(3)

    # Add 'Bike Light' and 'Fleece Jacket' to the cart
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
    time.sleep(3)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))).click()
    time.sleep(3)

    # Proceed to the cart
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="shopping_cart_container"]/a'))).click()
    time.sleep(3)

    # Checkout
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkout"]'))).click()
    time.sleep(3)

    # Enter checkout info
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="first-name"]'))).send_keys('Jonnathan')
    time.sleep(3)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="last-name"]'))).send_keys('K')
    time.sleep(3)
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="postal-code"]'))).send_keys('10007')
    time.sleep(3)

    # Continue and finish purchase
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="continue"]'))).click()
    time.sleep(3)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="finish"]'))).click()
    time.sleep(3)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="back-to-products"]'))).click()
    time.sleep(3)

    # Logout
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-burger-menu-btn"]'))).click()
    time.sleep(3)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="logout_sidebar_link"]'))).click()

    sys.exit(0)

except Exception as e:
    driver.save_screenshot('C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\failed_test.png')
    sys.exit(1)

finally:
    time.sleep(3)
    driver.quit()
