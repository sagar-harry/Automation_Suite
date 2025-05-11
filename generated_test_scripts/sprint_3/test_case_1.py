
import os
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

def login(driver, username, password):
    try:
        user_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user"]')))
        pass_field = driver.find_element(By.XPATH, '//*[@id="password"]')
        login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')
        user_field.send_keys(username)
        time.sleep(3)
        pass_field.send_keys(password)
        time.sleep(3)
        login_button.click()
    except Exception as e:
        print(f"Login failed: {e}")
        sys.exit(1)

def logout(driver):
    try:
        logout_sidebar = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="react-burger-menu-btn"]')))
        logout_sidebar.click()
        time.sleep(3)
        logout_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="logout_sidebar_link"]')))
        logout_button.click()
    except Exception as e:
        print(f"Logout failed: {e}")
        sys.exit(1)

def main():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")
    options.add_argument("--disable-features=NetworkService")
    
    driver = webdriver.Chrome(options=options)

    try:
        driver.maximize_window()
        driver.get("https://saucedemo.com/")
        time.sleep(5)

        login(driver, "standard", "secret_sauce")
        
        bike_light = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
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
        time.sleep(3)
        
        first_name_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="first-name"]')))
        last_name_field = driver.find_element(By.XPATH, '//*[@id="last-name"]')
        postal_code_field = driver.find_element(By.XPATH, '//*[@id="postal-code"]')
        first_name_field.send_keys("Jonnathan")
        time.sleep(3)
        last_name_field.send_keys("K")
        time.sleep(3)
        postal_code_field.send_keys("10007")
        time.sleep(3)
        
        continue_button = driver.find_element(By.XPATH, '//*[@id="continue"]')
        continue_button.click()
        time.sleep(3)

        finish_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="finish"]')))
        finish_button.click()
        time.sleep(3)

        back_to_products_button = driver.find_element(By.XPATH, '//*[@id="back-to-products"]')
        back_to_products_button.click()
        time.sleep(3)

        logout(driver)

        snapshot_path = "C:/Users/Administrator/Desktop/QE_COE/automated_pipeline_2/captured_screenshots"
        if not os.path.exists(snapshot_path):
            os.makedirs(snapshot_path)
        driver.save_screenshot(os.path.join(snapshot_path, "test_case_result.png"))
        
        print("Test case passed.")
        sys.exit(0)
        
    except Exception as e:
        snapshot_path = "C:/Users/Administrator/Desktop/QE_COE/automated_pipeline_2/captured_screenshots"
        if not os.path.exists(snapshot_path):
            os.makedirs(snapshot_path)
        driver.save_screenshot(os.path.join(snapshot_path, "test_case_error.png"))
        print(f"An error occurred: {e}")
        sys.exit(1)
        
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    main()
