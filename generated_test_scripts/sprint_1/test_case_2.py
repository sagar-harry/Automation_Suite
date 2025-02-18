
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.XPATH, "//*[@id='user-name']").send_keys(username)
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//*[@id='password']").send_keys(password)
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//*[@id='login-button']").click()
        time.sleep(3)

def setUp():
    chrome_options = Options()
    chrome_options.headless = True
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)
    return driver

def test_add_items_and_checkout():
    driver = setUp()
    
    try:
        driver.get("https://saucedemo.com/")
        driver.maximize_window()
        time.sleep(5)

        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        # Add Bike Light to cart
        driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']").click()
        time.sleep(3)

        # Add Fleece Jacket to cart
        driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']").click()
        time.sleep(3)
        
        # Go to cart
        driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a").click()
        time.sleep(3)

        # Proceed to checkout
        driver.find_element(By.XPATH, "//*[@id='checkout']").click()
        time.sleep(3)

        # Enter checkout information
        driver.find_element(By.XPATH, "//*[@id='first-name']").send_keys("somename")
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='last-name']").send_keys("lastname")
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='postal-code']").send_keys("123456")
        time.sleep(3)

        # Continue to Payment Information
        driver.find_element(By.XPATH, "//*[@id='continue']").click()
        time.sleep(3)

        # Verify Payment Information section is displayed
        payment_information = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[1]")
        if payment_information.is_displayed():
            print("Test Passed")
            exit(0)
        else:
            print("Test Failed")
            exit(1)
    
    except Exception as e:
        print(f"Test Failed due to exception: {e}")
        exit(1)
    
    finally:
        driver.quit()

test_add_items_and_checkout()
