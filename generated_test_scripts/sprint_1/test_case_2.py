
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import sys

def login(driver):
    driver.get("https://saucedemo.com/")
    time.sleep(5)
    
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

def wait_and_click(driver, by, path):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((by, path)))
    time.sleep(3)
    driver.find_element(by, path).click()

def wait_and_enter_text(driver, by, path, text):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((by, path)))
    time.sleep(3)
    driver.find_element(by, path).send_keys(text)

if __name__ == "__main__":
    try:
        options = Options()
        options.add_argument("--incognito")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-features=NetworkService")
        
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        
        login(driver)
        
        wait_and_click(driver, By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
        wait_and_click(driver, By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        wait_and_click(driver, By.XPATH, '//*[@id="shopping_cart_container"]/a')
        wait_and_click(driver, By.XPATH, '//*[@id="checkout"]')
        
        wait_and_enter_text(driver, By.XPATH, '//*[@id="first-name"]', "somename")
        wait_and_enter_text(driver, By.XPATH, '//*[@id="last-name"]', "lastname")
        wait_and_enter_text(driver, By.XPATH, '//*[@id="postal-code"]', "123456")

        wait_and_click(driver, By.XPATH, '//*[@id="continue"]')
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]'))
        )
        
        # Save snapshot
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\checkout_page.png")
        
        sys.exit(0)
    except Exception as e:
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\error_page.png")
        sys.exit(1)
    finally:
        driver.quit()
