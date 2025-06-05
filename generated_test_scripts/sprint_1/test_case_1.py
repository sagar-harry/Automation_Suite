
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import sys
import time

class LoginPage:
    def login(self, driver, username, password):
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        driver.maximize_window()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='user-name']"))).send_keys(username)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='password']"))).send_keys(password)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='login-button']"))).click()
        time.sleep(3)

def ui_test():
    options = Options()
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=options)

    try:
        lp = LoginPage()
        lp.login(driver, "standard_user", "secret_sauce")

        # Add items to cart
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']"))).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"))).click()
        time.sleep(3)

        # Verify cart badge
        cart_badge = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='shopping_cart_badge']")))
        assert cart_badge.text == '2', "Cart badge shows incorrect count"
        
        # Remove items from cart
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@id='remove-sauce-labs-bike-light']"))).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@id='remove-sauce-labs-fleece-jacket']"))).click()
        time.sleep(3)

        # Verify cart count element does not exist
        assert not driver.find_elements(By.XPATH, "//span[@class='shopping_cart_badge']"), "Cart badge still exists"

        # Add another item to cart
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"))).click()
        time.sleep(3)

        # Verify cart badge
        cart_badge = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='shopping_cart_badge']")))
        assert cart_badge.text == '1', "Cart badge shows incorrect count"

        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot.png")
        
        sys.exit(0)

    except Exception as e:
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\error_screenshot.png")
        print(f"An error occurred: {e}")
        sys.exit(1)
    finally:
        driver.quit()

ui_test()
