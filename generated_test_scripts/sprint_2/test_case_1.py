
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
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]'))
        ).send_keys(username)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

def main():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-features=NetworkService")
    
    driver = webdriver.Chrome(options=options)
    driver.get("https://saucedemo.com/")
    
    time.sleep(5)
    driver.maximize_window()
    time.sleep(3)
    
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    
    time.sleep(3)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
    ).click()
    
    time.sleep(3)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
    ).click()
    
    time.sleep(3)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a'))
    ).click()
    
    time.sleep(3)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="checkout"]'))
    ).click()

    time.sleep(3)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="first-name"]'))
    ).send_keys("Jonnathan")
    
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("K")
    driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("10007")
    
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="continue"]').click()
    
    time.sleep(3)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="finish"]'))
    ).click()
    
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="back-to-products"]').click()
    
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
    
    time.sleep(3)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="logout_sidebar_link"]'))
    ).click()
    
    time.sleep(3)
    driver.save_screenshot('C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot.png')
    
    driver.quit()
    sys.exit(0)

try:
    main()
except Exception as e:
    print(f"Test case failed due to: {e}")
    sys.exit(1)
