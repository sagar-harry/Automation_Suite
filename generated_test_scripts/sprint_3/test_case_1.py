
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import sys

def test_purchase_flow():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-features=NetworkService")
    
    driver = webdriver.Chrome(options=options)
    try:
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        driver.maximize_window()
        
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="user"]')))
        username_input = driver.find_element(By.XPATH, '//*[@id="user"]')
        password_input = driver.find_element(By.XPATH, '//*[@id="password"]')
        login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')
        
        username_input.send_keys("standard")
        time.sleep(3)
        password_input.send_keys("secret_sauce")
        time.sleep(3)
        login_button.click()
        
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
        bike_light = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
        fleece_jacket = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        
        bike_light.click()
        time.sleep(3)
        fleece_jacket.click()
        time.sleep(3)
        
        cart_icon = driver.find_element(By.XPATH, '//*[@id="123"]/a')
        cart_icon.click()
        time.sleep(3)
        
        checkout_button = driver.find_element(By.XPATH, '//*[@id="checkout"]')
        checkout_button.click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="first-name"]')))
        
        first_name_input = driver.find_element(By.XPATH, '//*[@id="first-name"]')
        last_name_input = driver.find_element(By.XPATH, '//*[@id="last-name"]')
        postal_code_input = driver.find_element(By.XPATH, '//*[@id="postal-code"]')
        
        first_name_input.send_keys("Jonnathan")
        time.sleep(3)
        last_name_input.send_keys("K")
        time.sleep(3)
        postal_code_input.send_keys("10007")
        time.sleep(3)
        
        continue_button = driver.find_element(By.XPATH, '//*[@id="continue"]')
        continue_button.click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="finish"]')))
        
        finish_button = driver.find_element(By.XPATH, '//*[@id="finish"]')
        finish_button.click()
        time.sleep(3)

        back_to_products = driver.find_element(By.XPATH, '//*[@id="back-to-products"]')
        back_to_products.click()
        time.sleep(3)
        
        logout_sidebar = driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]')
        logout_sidebar.click()
        time.sleep(3)
        
        logout_button = driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]')
        logout_button.click()
        time.sleep(3)
        
        # Take a snapshot
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\test_screenshot.png")
        
        sys.exit(0)

    except Exception as e:
        print(e)
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\error_screenshot.png")
        sys.exit(1)
    finally:
        driver.quit()

test_purchase_flow()
