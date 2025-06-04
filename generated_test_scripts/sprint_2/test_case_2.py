
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']"))).send_keys(username)
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@id='login-button']").click()

def main():
    try:
        # Setup Chrome options
        options = Options()
        options.add_argument("--incognito")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_argument('--disable-features=NetworkService')
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")

        # Initialize WebDriver
        driver = webdriver.Chrome(options=options)
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        driver.maximize_window()

        # Login
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        # Add "Bike Light" to the cart
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']"))).click()
        time.sleep(3)

        # Add "Fleece Jacket" to the cart
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"))).click()
        time.sleep(3)

        # Verify cart badge
        cart_badge = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='shopping_cart_badge']")))
        if cart_badge.text == '2':
            print("Test Passed: Cart badge displays '2'")
            driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\test_passed.png")
            sys.exit(0)
        else:
            print("Test Failed: Cart badge does not display '2'")
            driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\test_failed.png")
            sys.exit(1)

    except Exception as e:
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\exception.png")
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
