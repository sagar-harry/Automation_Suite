
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

def login(driver, username, password):
    driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys(username)
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@id='login-button']").click()
    time.sleep(3)

def main():
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-notifications')
    options.add_argument('--incognito')
    options.add_argument('--disable-features=NetworkService')

    driver = webdriver.Chrome(options=options)
    driver.get('https://saucedemo.com/')
    time.sleep(5)
    driver.maximize_window()

    try:
        login(driver, 'standard_user', 'secret_sauce')

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']"))).click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@id='checkout']").click()
        time.sleep(3)

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='first-name']"))).send_keys('Jonnathan')
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='last-name']").send_keys('K')
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='postal-code']").send_keys('10007')
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='continue']").click()
        time.sleep(3)

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[text()='Payment Information']")))

        sys.exit(0)
    except Exception as e:
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\error.png")
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
