
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
        self.driver.get("https://saucedemo.com/")
        self.driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys(username)
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)
        self.driver.find_element(By.XPATH, "//input[@id='login-button']").click()

def take_screenshot(driver):
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")

def main():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=options)

    try:
        driver.maximize_window()
        driver.get("https://saucedemo.com/")
        time.sleep(5)  # Wait 5 seconds before starting the test

        # Login
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        wait = WebDriverWait(driver, 10)

        # Add Bike Light and Fleece Jacket to the cart
        time.sleep(3)
        wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']"))).click()

        time.sleep(3)
        wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"))).click()

        # Check cart badge count
        time.sleep(3)
        cart_badge = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='shopping_cart_badge']")))
        assert cart_badge.text == '2', f"Expected cart badge to be '2', but got {cart_badge.text}"

        # Remove Bike Light and Fleece Jacket
        time.sleep(3)
        wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='remove-sauce-labs-bike-light']"))).click()

        time.sleep(3)
        wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='remove-sauce-labs-fleece-jacket']"))).click()

        # Check that cart badge does not exist
        time.sleep(3)
        assert not driver.find_elements(By.XPATH, "//span[@class='shopping_cart_badge']"), "Cart badge should not exist"

        # Add Bolt T-Shirt to the cart
        time.sleep(3)
        wait.until(EC.presence_of_element_located((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"))).click()

        time.sleep(3)
        cart_badge = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='shopping_cart_badge']")))
        assert cart_badge.text == '1', f"Expected cart badge to be '1', but got {cart_badge.text}"

        sys.exit(0)
    except Exception as e:
        take_screenshot(driver)
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
