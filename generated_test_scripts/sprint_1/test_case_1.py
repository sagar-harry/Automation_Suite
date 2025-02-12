
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def open_site():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--incognito')
    options.add_argument('--disable-notifications')
    driver = webdriver.Chrome(options=options)
    driver.get("https://saucedemo.com/")
    time.sleep(5)
    driver.maximize_window()
    return driver

def login(driver, username, password):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]'))
    ).send_keys(username)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))
    ).send_keys(password)
    time.sleep(3)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]'))
    ).click()
    time.sleep(3)

def add_to_cart(driver, product_xpath):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, product_xpath))
    ).click()
    time.sleep(3)

def reset_cart(driver):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="shopping_cart_container"]/a'))
    ).click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="cart_contents_container"]/div/div[2]/div[1]/button').click() # Assumes reset button is present at this location
    time.sleep(3)

def verify_cart_badge(driver, expected_count):
    badge = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
    )
    assert badge.text == expected_count, f"Failed: Expected {expected_count}, but got {badge.text}"

def test_scenario():
    driver = open_site()
    try:
        login(driver, "standard_user", "secret_sauce")

        add_to_cart(driver, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
        add_to_cart(driver, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        verify_cart_badge(driver, '2')

        reset_cart(driver)
        verify_cart_badge(driver, '0')

        add_to_cart(driver, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        verify_cart_badge(driver, '1')

        driver.quit()
        exit(0)
    except AssertionError as e:
        print(e)
        driver.quit()
        exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        driver.quit()
        exit(1)

if __name__ == "__main__":
    test_scenario()
