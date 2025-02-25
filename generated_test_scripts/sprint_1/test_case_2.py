
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver, username, password):
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(3)

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-notifications')
options.add_argument('--disable-popup-blocking')
options.add_argument('--incognito')
options.add_argument('--disable-features=NetworkService')

driver = webdriver.Chrome(options=options)
driver.get("https://saucedemo.com/")
time.sleep(5)
driver.maximize_window()

try:
    wait = WebDriverWait(driver, 10)
    
    login(driver, "standard_user", "secret_sauce")
    
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
    time.sleep(3)
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))).click()
    time.sleep(3)
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a'))).click()
    time.sleep(3)
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="checkout"]'))).click()
    time.sleep(3)

    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="first-name"]'))).send_keys("somename")
    time.sleep(3)
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="last-name"]'))).send_keys("lastname")
    time.sleep(3)
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="postal-code"]'))).send_keys("123456")
    time.sleep(3)
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="continue"]'))).click()
    time.sleep(3)

    if wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]'))):
        print("Payment Information label is visible.")
        sys.exit(0)
    else:
        print("Payment Information label is not visible.")
        sys.exit(1)

except Exception as e:
    print(f"Test failed: {e}")
    sys.exit(1)

finally:
    driver.quit()
