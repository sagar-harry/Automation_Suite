
import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--incognito")
options.add_argument("--disable-notifications")
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-features=NetworkService")

try:
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)

    driver.get('https://saucedemo.com/')
    time.sleep(5)

    # Login
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys('standard_user')
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(3)

    # Add Bike Light
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
    time.sleep(3)

    # Add Fleece Jacket
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]'))).click()
    time.sleep(3)

    # Verify Cart Badge displays '2'
    cart_badge = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text
    assert cart_badge == '2', f"Expected cart badge to be '2', but got {cart_badge}"

    # Remove Bike Light
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]'))).click()
    time.sleep(3)

    # Remove Fleece Jacket
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]'))).click()
    time.sleep(3)

    # Verify Cart Count Element doesn't exist
    assert len(driver.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')) == 0, "Cart count element should not exist"

    # Add Bolt T-Shirt
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))).click()
    time.sleep(3)

    # Verify Cart Badge displays '1'
    cart_badge = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span').text
    assert cart_badge == '1', f"Expected cart badge to be '1', but got {cart_badge}"

    time.sleep(3)
    driver.save_screenshot(r'C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png')

    sys.exit(0)

except Exception as e:
    driver.save_screenshot(r'C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\error_screenshot.png')
    sys.exit(1)

finally:
    driver.quit()
