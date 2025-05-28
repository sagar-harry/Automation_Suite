
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import sys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.XPATH, '//*[@id="user"]').send_keys(username)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

def run_test():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-features=NetworkService")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    
    driver = webdriver.Chrome(options=options)
    driver.get("https://saucedemo.com/")
    
    time.sleep(5)
    driver.maximize_window()
    
    try:
        login_page = LoginPage(driver)
        time.sleep(3)
        login_page.login("standard", "secret_sauce")

        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="123"]/a').click()
        
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
        
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys('Jonnathan')
        driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys('K')
        driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys('10007')
        
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="continue"]').click()
        
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="finish"]').click()
        
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
        
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]').click()

        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")
        sys.exit(0)
    except Exception as e:
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot_failed.png")
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    run_test()
