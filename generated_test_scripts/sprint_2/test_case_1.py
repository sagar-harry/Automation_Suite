
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

def setup_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-features=NetworkService")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    return driver

def wait_and_find_element(driver, by, value):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((by, value)))
    time.sleep(3)
    return driver.find_element(by, value)

def login(driver, username, password):
    driver.get("https://saucedemo.com/")
    time.sleep(5)

    wait_and_find_element(driver, By.XPATH, '//*[@id="user-name"]').send_keys(username)
    wait_and_find_element(driver, By.XPATH, '//*[@id="password"]').send_keys(password)
    wait_and_find_element(driver, By.XPATH, '//*[@id="login-button"]').click()

def logout(driver):
    wait_and_find_element(driver, By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
    wait_and_find_element(driver, By.XPATH, '//*[@id="logout_sidebar_link"]').click()

def add_to_cart(driver):
    wait_and_find_element(driver, By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
    wait_and_find_element(driver, By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()

def checkout(driver):
    wait_and_find_element(driver, By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
    wait_and_find_element(driver, By.XPATH, '//*[@id="checkout"]').click()
    wait_and_find_element(driver, By.XPATH, '//*[@id="first-name"]').send_keys('somename')
    wait_and_find_element(driver, By.XPATH, '//*[@id="last-name"]').send_keys('lastname')
    wait_and_find_element(driver, By.XPATH, '//*[@id="postal-code"]').send_keys('123456')
    wait_and_find_element(driver, By.XPATH, '//*[@id="continue"]').click()
    wait_and_find_element(driver, By.XPATH, '//*[@id="finish"]').click()
    wait_and_find_element(driver, By.XPATH, '//*[@id="back-to-products"]')

def test_purchase_flow():
    driver = setup_driver()
    try:
        login(driver, 'standard_user', 'secret_sauce')
        add_to_cart(driver)
        checkout(driver)
        logout(driver)
        driver.quit()
        sys.exit(0)
    except Exception as e:
        print(f"Test failed: {e}")
        driver.quit()
        sys.exit(1)

if __name__ == "__main__":
    test_purchase_flow()
