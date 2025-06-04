
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    @staticmethod
    def login(driver, username, password):
        driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys(username)
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)
        driver.find_element(By.XPATH, "//input[@id='login-button']").click()

def test_purchase_flow():
    options = Options()
    options.add_argument("--incognito")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        driver.maximize_window()
        
        LoginPage.login(driver, "standard", "secret_sauce")
        time.sleep(3)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']"))).click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"))).click()
        time.sleep(3)
        
        driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
        time.sleep(3)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='checkout']"))).click()
        time.sleep(3)

        driver.find_element(By.XPATH, "//input[@id='first-name']").send_keys("Jonnathan")
        driver.find_element(By.XPATH, "//input[@id='last-name']").send_keys("K")
        driver.find_element(By.XPATH, "//input[@id='postal-code']").send_keys("10007")
        driver.find_element(By.XPATH, "//input[@id='continue']").click()
        time.sleep(3)

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='finish']"))).click()
        time.sleep(3)

        driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//a[@id='logout_sidebar_link']").click()
        
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")
        sys.exit(0)
    
    except Exception as e:
        print(f"Test failed: {e}")
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")
        sys.exit(1)
    
    finally:
        driver.quit()

if __name__ == "__main__":
    test_purchase_flow()
