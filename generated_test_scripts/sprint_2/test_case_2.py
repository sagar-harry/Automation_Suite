
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys(username)
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)
        self.driver.find_element(By.XPATH, "//input[@id='login-button']").click()

try:
    # Setup Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-features=NetworkService")
    
    # Initialize WebDriver
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    # Navigate to website
    driver.get("https://saucedemo.com/")
    time.sleep(5)  # Wait for 5 seconds after opening the page

    # Login
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    time.sleep(3)  # Wait for 3 seconds for login action

    # Add "Bike Light" to cart
    bike_light_add = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']"))
    )
    bike_light_add.click()
    time.sleep(3)  # Wait for 3 seconds

    # Add "Fleece Jacket" to cart
    fleece_jacket_add = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"))
    )
    fleece_jacket_add.click()
    time.sleep(3)  # Wait for 3 seconds

    # Verify cart badge displays '2'
    cart_badge = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='shopping_cart_badge']"))
    )
    
    if cart_badge.text == "2":
        sys.exit(0)
    else:
        raise Exception("Cart badge does not display '2'")

except Exception as e:
    driver.get_screenshot_as_file("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\failed_test.png")
    sys.exit(1)
finally:
    driver.quit()
