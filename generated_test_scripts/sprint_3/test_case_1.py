
import time
import sys
import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        user_name_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@id='user-name']"))
        )
        password_field = self.driver.find_element(By.XPATH, "//input[@id='password']")
        login_button = self.driver.find_element(By.XPATH, "//input[@id='login-button']")
        
        time.sleep(3)
        user_name_field.send_keys(username)
        time.sleep(3)
        password_field.send_keys(password)
        time.sleep(3)
        login_button.click()

    def logout(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@id='react-burger-menu-btn']"))
        ).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[@id='logout_sidebar_link']").click()

def test_complete_purchase_flow():
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://saucedemo.com/")
    time.sleep(5)
    driver.maximize_window()

    try:
        login_page = LoginPage(driver)
        login_page.login("standard", "secret_sauce")

        # Add 'Bike Light' and 'Fleece Jacket' to cart
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']"))
        ).click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']").click()
        time.sleep(3)

        # Proceed to cart
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@class='shopping_cart_link']"))
        ).click()
        time.sleep(3)

        # Proceed to checkout
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@id='checkout']"))
        ).click()
        time.sleep(3)

        # Enter checkout information
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@id='first-name']"))
        ).send_keys("Jonnathan")
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='last-name']").send_keys("K")
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='postal-code']").send_keys("10007")
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='continue']").click()
        time.sleep(3)

        # Finish purchase
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@id='finish']"))
        ).click()
        time.sleep(3)

        # Return to homepage
        driver.find_element(By.XPATH, "//button[@id='back-to-products']").click()
        time.sleep(3)

        # Logout
        login_page.logout()

        # Capture screenshot
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot.png")

        sys.exit(0)

    except Exception as e:
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\error_screenshot.png")
        traceback.print_exc()
        sys.exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    test_complete_purchase_flow()
