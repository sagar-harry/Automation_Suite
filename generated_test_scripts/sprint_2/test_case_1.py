
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def main():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-notifications')
    options.add_argument('--disable-extensions')
    options.add_argument('--incognito')

    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get('https://saucedemo.com/')
        time.sleep(5)
        driver.maximize_window()

        # Login
        login(driver)

        # Add products to cart
        add_to_cart(driver)

        # Checkout Process
        checkout(driver)

        # Logout
        logout(driver)

        print("Test completed successfully.")
        exit(0)  # Indicate success

    except Exception as e:
        print(f"Test failed: {e}")
        exit(1)  # Indicate failure

    finally:
        driver.quit()

def login(driver):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]'))).send_keys('standard_user')
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(3)

def add_to_cart(driver):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))).click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
    time.sleep(3)

def checkout(driver):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="checkout"]'))).click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys('somename')
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys('lastname')
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys('123456')
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="continue"]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="finish"]').click()
    time.sleep(3)

def logout(driver):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="back-to-products"]'))).click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="logout_sidebar_link"]'))).click()
    time.sleep(3)

if __name__ == "__main__":
    main()
