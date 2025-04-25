
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        
    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='user-name']"))).send_keys(username)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='password']"))).send_keys(password)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='login-button']"))).click()
        time.sleep(3)

def test_checkout_process():
    url = "https://saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(url)
    
    time.sleep(5)
    
    try:
        login_page = LoginPage(driver)
        login_page.login(username, password)
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']"))).click()
        time.sleep(3)
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']"))).click()
        time.sleep(3)
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='shopping_cart_container']/a"))).click()
        time.sleep(3)
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='checkout']"))).click()
        time.sleep(3)
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='first-name']"))).send_keys("Jonnathan")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='last-name']"))).send_keys("K")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='postal-code']"))).send_keys("10007")
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='continue']"))).click()
        time.sleep(3)
        
        payment_information = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[1]")))
        assert payment_information.is_displayed(), "Payment Information label not found"
        
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\payment_info_visible.png")

    except Exception as e:
        print(f"Test failed: {str(e)}")
        driver.quit()
        sys.exit(1)
    else:
        print("Test passed")
        driver.quit()
        sys.exit(0)

if __name__ == "__main__":
    test_checkout_process()
