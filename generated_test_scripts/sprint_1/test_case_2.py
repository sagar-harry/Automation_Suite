
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import sys

def login(driver, username, password):
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(3)

def run_test():
    url = "https://saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-features=NetworkService")
    chrome_options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    time.sleep(5)
    driver.maximize_window()

    login(driver, username, password)
    
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
    time.sleep(3)

    driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys('somename')
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys('lastname')
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys('123456')
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="continue"]').click()
    time.sleep(3)

    payment_information_visible = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]').is_displayed()

    driver.quit()
    
    if payment_information_visible:
        sys.exit(0)
    else:
        sys.exit(1)

run_test()
