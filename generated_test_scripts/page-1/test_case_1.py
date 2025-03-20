
import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver):
    username_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]')))
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//*[@id="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')
    login_button.click()

def test_payment_information_visible():
    try:
        chrome_options = Options()
        chrome_options.add_argument('--disable-notifications')
        chrome_options.add_argument('--incognito')
        chrome_options.add_argument('--disable-features=NetworkService')

        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.get("https://saucedemo.com/")
        sleep(5)

        login(driver)
        sleep(3)

        bike_light = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
        bike_light.click()
        sleep(3)

        fleece_jacket = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        fleece_jacket.click()
        sleep(3)

        cart_icon = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
        cart_icon.click()
        sleep(3)

        checkout_button = driver.find_element(By.XPATH, '//*[@id="checkout"]')
        checkout_button.click()
        sleep(3)

        first_name = driver.find_element(By.XPATH, '//*[@id="first-name"]')
        first_name.send_keys("Jonnathan")
        sleep(3)

        last_name = driver.find_element(By.XPATH, '//*[@id="last-name"]')
        last_name.send_keys("K")
        sleep(3)

        zip_code = driver.find_element(By.XPATH, '//*[@id="postal-code"]')
        zip_code.send_keys("10007")
        sleep(3)

        continue_button = driver.find_element(By.XPATH, '//*[@id="continue"]')
        continue_button.click()
        sleep(3)

        payment_information = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]')))
        
        if payment_information.is_displayed():
            print("Payment Information label is visible.")
            driver.save_screenshot('C:/Users/Administrator/Desktop/QE_COE/automated_pipeline_2/captured_screenshots/success.png')
            sys.exit(0)
        else:
            driver.save_screenshot('C:/Users/Administrator/Desktop/QE_COE/automated_pipeline_2/captured_screenshots/failure.png')
            sys.exit(1)

    except Exception as e:
        print(f"An exception occurred: {e}")
        driver.save_screenshot('C:/Users/Administrator/Desktop/QE_COE/automated_pipeline_2/captured_screenshots/error.png')
        sys.exit(1)

    finally:
        driver.quit()

test_payment_information_visible()
