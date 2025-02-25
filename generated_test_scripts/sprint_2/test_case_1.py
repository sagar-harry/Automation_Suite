
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-features=NetworkService")

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)

def wait_and_find(by, locator):
    return WebDriverWait(driver, 10).until(EC.presence_of_element_located((by, locator)))

try:
    # Open the website
    driver.get("https://saucedemo.com/")
    time.sleep(5)
    driver.maximize_window()

    # Log in
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
    time.sleep(3)
    wait_and_find(By.XPATH, '//*[@id="login-button"]').click()

    # Add items to the cart
    time.sleep(3)
    wait_and_find(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
    time.sleep(3)
    wait_and_find(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()

    # Proceed to checkout
    time.sleep(3)
    wait_and_find(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
    time.sleep(3)
    wait_and_find(By.XPATH, '//*[@id="checkout"]').click()

    # Enter user details
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys("somename")
    driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("lastname")
    driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("123456")
    time.sleep(3)
    wait_and_find(By.XPATH, '//*[@id="continue"]').click()

    # Finish purchase
    time.sleep(3)
    wait_and_find(By.XPATH, '//*[@id="finish"]').click()

    # Return to homepage
    time.sleep(3)
    wait_and_find(By.XPATH, '//*[@id="back-to-products"]').click()

    # Log out
    time.sleep(3)
    wait_and_find(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
    time.sleep(3)
    wait_and_find(By.XPATH, '//*[@id="logout_sidebar_link"]').click()

    sys.exit(0)
except Exception as e:
    print(f"Test failed: {e}")
    sys.exit(1)
finally:
    driver.quit()
