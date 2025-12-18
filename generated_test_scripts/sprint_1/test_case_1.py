
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

class LoginPage:
    def login(self, driver, username, password):
        user_input = driver.find_element(By.XPATH, "//input[@id='user-name']")
        password_input = driver.find_element(By.XPATH, "//input[@id='password']")
        login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
        
        user_input.send_keys(username)
        password_input.send_keys(password)
        login_button.click()

def test_ui_scenario():
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-features=NetworkService")
        
        driver = webdriver.Chrome(options=options)
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        driver.maximize_window()
        
        login_page = LoginPage()
        login_page.login(driver, "standard_user", "secret_sauce")
        time.sleep(3)
        
        # Add 'Bike Light' to the cart
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']"))
        ).click()
        time.sleep(3)
        
        # Add 'Fleece Jacket' to the cart
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"))
        ).click()
        time.sleep(3)
        
        # Verify cart badge displays '2'
        cart_badge = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[@class='shopping_cart_badge']"))
        )
        assert cart_badge.text == '2'
        time.sleep(3)
        
        # Remove 'Bike Light'
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='remove-sauce-labs-bike-light']"))
        ).click()
        time.sleep(3)
        
        # Remove 'Fleece Jacket'
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='remove-sauce-labs-fleece-jacket']"))
        ).click()
        time.sleep(3)
        
        # Verify cart count element shouldn't exist
        assert not driver.find_elements(By.XPATH, "//span[@class='shopping_cart_badge']")
        time.sleep(3)
        
        # Add 'Bolt T-Shirt' to the cart
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"))
        ).click()
        time.sleep(3)
        
        # Verify cart badge displays '1'
        cart_badge = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[@class='shopping_cart_badge']"))
        )
        assert cart_badge.text == '1'
        
        # Save snapshot of the page
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\final_screenshot.png")
        
        driver.quit()
        sys.exit(0)
        
    except Exception as e:
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\error_screenshot.png")
        driver.quit()
        sys.exit(1)

if __name__ == "__main__":
    test_ui_scenario()
