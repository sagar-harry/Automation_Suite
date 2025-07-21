
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def login(driver, username, password):
    driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys(username)
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)
    driver.find_element(By.XPATH, "//input[@id='login-button']").click()

try:
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.saucedemo.com/")
    time.sleep(5)
    driver.maximize_window()

    login(driver, username="standard_user", password="secret_sauce")

    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']"))).click()
    
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"))).click()
    
    time.sleep(3)
    cart_badge = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='shopping_cart_badge']")))
    assert cart_badge.text == '2', "Cart badge is not displaying '2'"

    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='remove-sauce-labs-bike-light']"))).click()
    
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='remove-sauce-labs-fleece-jacket']"))).click()
    
    time.sleep(3)
    assert len(driver.find_elements(By.XPATH, "//span[@class='shopping_cart_badge']")) == 0, "Cart badge element should not exist"

    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']"))).click()
    
    time.sleep(3)
    cart_badge = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='shopping_cart_badge']")))
    assert cart_badge.text == '1', "Cart badge is not displaying '1'"

    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")
    sys.exit(0)

except Exception as e:
    driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot_error.png")
    sys.exit(1)
finally:
    driver.quit()
