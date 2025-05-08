
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import sys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    
    def login(self, username, password):
        self.driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

def take_screenshot(driver):
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")

try:
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://saucedemo.com/")
    time.sleep(5)
    driver.maximize_window()

    login_page = LoginPage(driver)
    time.sleep(3)
    
    # Login
    login_page.login(username="standard_user", password="secret_sauce")
    time.sleep(3)

    # Add Bike Light to Cart
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
    time.sleep(3)

    # Add Fleece Jacket to Cart
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]').click()
    time.sleep(3)

    # Verify Cart Badge Display '2'
    cart_badge = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    assert cart_badge.text == '2', "Cart badge does not display '2'"

    # Remove Bike Light
    driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]').click()
    time.sleep(3)

    # Remove Fleece Jacket
    driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]').click()
    time.sleep(3)

    # Verify Cart Count Element Does Not Exist
    assert len(driver.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')) == 0, "Cart count element still exists"

    # Add Bolt T-Shirt to Cart
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    time.sleep(3)

    # Verify Cart Badge Display '1'
    cart_badge = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    assert cart_badge.text == '1', "Cart badge does not display '1'"

    take_screenshot(driver)
    sys.exit(0)

except Exception as e:
    take_screenshot(driver)
    print(f"Test failed due to {e}")
    sys.exit(1)

finally:
    driver.quit()
