
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def take_screenshot(driver):
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")

try:
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://saucedemo.com/")
    time.sleep(5)

    wait = WebDriverWait(driver, 10)

    # Login
    from login_page import LoginPage  # Assuming the login method is defined here
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    time.sleep(3)

    # Add Bike Light
    bike_light_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
    bike_light_btn.click()
    time.sleep(3)

    # Add Fleece Jacket
    fleece_jacket_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]')))
    fleece_jacket_btn.click()
    time.sleep(3)

    # Check cart badge 2
    cart_count = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
    assert cart_count.text == '2'

    # Remove Bike Light
    remove_bike_light_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]')))
    remove_bike_light_btn.click()
    time.sleep(3)

    # Remove Fleece Jacket
    remove_fleece_jacket_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]')))
    remove_fleece_jacket_btn.click()
    time.sleep(3)

    # Check cart count doesn't exist
    assert not wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))

    # Add Bolt T-Shirt
    bolt_tshirt_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')))
    bolt_tshirt_btn.click()
    time.sleep(3)

    # Check cart badge 1
    cart_count = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
    assert cart_count.text == '1'

    take_screenshot(driver)
    sys.exit(0)

except Exception as e:
    take_screenshot(driver)
    sys.exit(1)

finally:
    driver.quit()
