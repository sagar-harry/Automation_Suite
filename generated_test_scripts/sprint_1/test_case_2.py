
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

def main():
    try:
        # Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument('--disable-features=NetworkService')
        
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.get("https://saucedemo.com/")
        time.sleep(5)

        # LoginPage class - login method
        driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
        time.sleep(3)

        # Add Bike Light and Fleece Jacket to the cart
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')))
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        time.sleep(3)

        # Proceed to checkout
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a')))
        driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="checkout"]')))
        driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
        time.sleep(3)

        # Enter checkout details
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="first-name"]')))
        driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys("Jonnathan")
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("K")
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("10007")
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="continue"]').click()
        time.sleep(3)

        # Validate Payment Information label
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]')))
        print("Test Passed: Payment Information label is visible")
        driver.save_screenshot(r'C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png')
        sys.exit(0)

    except Exception as e:
        print(f"Test Failed: {e}")
        driver.save_screenshot(r'C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png')
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
