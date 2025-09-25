
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    
    def login(self, username, password):
        self.driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys(username)
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)
        self.driver.find_element(By.XPATH, "//input[@id='login-button']").click()

def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popups")
    chrome_options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://saucedemo.com")
    time.sleep(5)
    driver.maximize_window()
    return driver

def test_reset_functionality():
    try:
        driver = setup_driver()
        wait = WebDriverWait(driver, 10)

        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        time.sleep(3)

        # Add Bike Light to the cart
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']"))).click()
        time.sleep(3)

        # Add Fleece Jacket to the cart
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"))).click()
        time.sleep(3)

        # Verify the cart badge displays '2'
        cart_badge = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='shopping_cart_badge']")))
        assert cart_badge.text == '2', "Cart badge count is incorrect"
        
        # Remove Bike Light
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='remove-sauce-labs-bike-light']"))).click()
        time.sleep(3)

        # Remove Fleece Jacket
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='remove-sauce-labs-fleece-jacket']"))).click()
        time.sleep(3)

        # Verify cart badge does not exist
        assert len(driver.find_elements(By.XPATH, "//span[@class='shopping_cart_badge']")) == 0, "Cart badge still exists"
        
        # Add Bolt T-Shirt
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"))).click()
        time.sleep(3)

        # Verify the cart badge displays '1'
        cart_badge = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='shopping_cart_badge']")))
        assert cart_badge.text == '1', "Cart badge count is incorrect"

        # Save page snapshot
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\snapshot.png")

        driver.quit()
        sys.exit(0)

    except Exception as e:
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\error_snapshot.png")
        driver.quit()
        sys.exit(1)

if __name__ == "__main__":
    test_reset_functionality()
