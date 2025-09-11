
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

options = Options()
options.add_argument("--incognito")
options.add_argument("--disable-notifications")
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-features=NetworkService")

try:
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://saucedemo.com/")
    time.sleep(5)
    
    wait = WebDriverWait(driver, 10)

    # Login
    wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='user-name']"))).send_keys("standard_user")
    time.sleep(3)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='password']"))).send_keys("secret_sauce")
    time.sleep(3)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='login-button']"))).click()
    time.sleep(3)

    # Adding items to cart
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']"))).click()
    time.sleep(3)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"))).click()
    time.sleep(3)

    # Proceed to Checkout
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='checkout']"))).click()
    time.sleep(3)

    # Enter user details
    wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='first-name']"))).send_keys("Jonnathan")
    time.sleep(3)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='last-name']"))).send_keys("K")
    time.sleep(3)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='postal-code']"))).send_keys("10007")
    time.sleep(3)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='continue']"))).click()
    time.sleep(3)

    # Verify Payment Information label
    payment_info_visible = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[text()='Payment Information']"))).is_displayed()
    
    if payment_info_visible:
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot.png")
        sys.exit(0)
    else:
        sys.exit(1)

except Exception as e:
    print(repr(e))
    sys.exit(1)

finally:
    driver.quit()
