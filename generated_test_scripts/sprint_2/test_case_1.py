
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = "https://saucedemo.com/"
username = "standard_user"
password = "secret_sauce"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-features=NetworkService")

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get(url)
    time.sleep(5)
    driver.maximize_window()

    def wait_for_element(by, locator):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((by, locator)))

    wait_for_element(By.XPATH, '//*[@id="user-name"]')
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
    time.sleep(3)

    wait_for_element(By.XPATH, '//*[@id="password"]')
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    time.sleep(3)

    wait_for_element(By.XPATH, '//*[@id="login-button"]')
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(3)

    wait_for_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
    time.sleep(3)

    wait_for_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    time.sleep(3)

    wait_for_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
    driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
    time.sleep(3)

    wait_for_element(By.XPATH, '//*[@id="checkout"]')
    driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
    time.sleep(3)

    wait_for_element(By.XPATH, '//*[@id="first-name"]')
    driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys('somename')
    time.sleep(3)

    wait_for_element(By.XPATH, '//*[@id="last-name"]')
    driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys('lastname')
    time.sleep(3)

    wait_for_element(By.XPATH, '//*[@id="postal-code"]')
    driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys('123456')
    time.sleep(3)

    wait_for_element(By.XPATH, '//*[@id="continue"]')
    driver.find_element(By.XPATH, '//*[@id="continue"]').click()
    time.sleep(3)

    wait_for_element(By.XPATH, '//*[@id="finish"]')
    driver.find_element(By.XPATH, '//*[@id="finish"]').click()
    time.sleep(3)

    wait_for_element(By.XPATH, '//*[@id="back-to-products"]')
    driver.find_element(By.XPATH, '//*[@id="back-to-products"]').click()
    time.sleep(3)

    wait_for_element(By.XPATH, '//*[@id="react-burger-menu-btn"]')
    driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
    time.sleep(3)

    wait_for_element(By.XPATH, '//*[@id="logout_sidebar_link"]')
    driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]').click()
    time.sleep(3)

    driver.quit()
    exit(0)
except Exception as e:
    print(f"Test failed: {e}")
    driver.quit()
    exit(1)
