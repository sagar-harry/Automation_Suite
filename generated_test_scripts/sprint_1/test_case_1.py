
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
import os

def configure_driver():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-features=NetworkService")
    driver = webdriver.Chrome(options=options)
    return driver

def save_screenshot(driver, script_name):
    screenshot_path = os.path.join("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots",
                                   f"{script_name}_screenshot.png")
    driver.save_screenshot(screenshot_path)

def login(driver, wait):
    driver.get("https://saucedemo.com/")
    time.sleep(5)
    driver.maximize_window()
    time.sleep(3)

    username_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]')))
    password_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]')))
    login_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="login-button"]')))
    
    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")
    login_button.click()
    
    time.sleep(3)

def test_cart_operations(driver, wait):
    bike_light = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
    fleece_jacket = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]')))
    
    bike_light.click()
    time.sleep(3)
    fleece_jacket.click()
    time.sleep(3)
    
    cart_count = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
    assert cart_count.text == '2'
    
    remove_bike_light = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]')))
    remove_fleece_jacket = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]')))
    
    remove_bike_light.click()
    time.sleep(3)
    remove_fleece_jacket.click()
    time.sleep(3)
    
    assert not driver.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    
    add_bolt_tshirt = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')))
    add_bolt_tshirt.click()
    time.sleep(3)
    
    cart_count = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
    assert cart_count.text == '1'
    
if __name__ == "__main__":
    driver = configure_driver()
    wait = WebDriverWait(driver, 10)

    try:
        login(driver, wait)
        test_cart_operations(driver, wait)
        sys.exit(0)
    except Exception as e:
        print(f"Test failed: {e}")
        sys.exit(1)
    finally:
        save_screenshot(driver, os.path.splitext(os.path.basename(__file__))[0])
        driver.quit()
