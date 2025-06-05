
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def login(driver, username, password):
    driver.get("https://saucedemo.com/")
    time.sleep(5)
    driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys(username)
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)
    driver.find_element(By.XPATH, "//input[@id='login-button']").click()
    time.sleep(3)

try:
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-features=NetworkService")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    login(driver, "standard_user", "secret_sauce")

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']"))).click()
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"))).click()
    time.sleep(3)

    driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
    time.sleep(3)

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@id='checkout']"))).click()
    time.sleep(3)

    driver.find_element(By.XPATH, "//input[@id='first-name']").send_keys("Jonnathan")
    driver.find_element(By.XPATH, "//input[@id='last-name']").send_keys("K")
    driver.find_element(By.XPATH, "//input[@id='postal-code']").send_keys("10007")
    time.sleep(3)

    driver.find_element(By.XPATH, "//input[@id='continue']").click()
    time.sleep(3)

    payment_info = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Payment Information')]")))

    if payment_info.is_displayed():
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")
        sys.exit(0)

except Exception as e:
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")
    sys.exit(1)

finally:
    driver.quit()
