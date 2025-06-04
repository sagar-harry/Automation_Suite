
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def test_payment_information_visibility():
    try:
        # Set up Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-features=NetworkService")

        driver = webdriver.Chrome(options=chrome_options)
        
        # Load the website
        driver.get("https://saucedemo.com/")
        time.sleep(5)

        driver.maximize_window()

        # User Login
        driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='login-button']").click()
        
        # Add 'Bike Light' to cart
        add_bike_light_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']"))
        )
        add_bike_light_button.click()
        time.sleep(3)

        # Add 'Fleece Jacket' to cart
        add_fleece_jacket_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"))
        )
        add_fleece_jacket_button.click()
        time.sleep(3)

        # Proceed to checkout
        checkout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='checkout']"))
        )
        checkout_button.click()
        time.sleep(3)

        # Enter checkout information
        driver.find_element(By.XPATH, "//input[@id='first-name']").send_keys("Jonnathan")
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='last-name']").send_keys("K")
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='postal-code']").send_keys("10007")
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='continue']").click()

        # Validate payment information visibility
        payment_info_label = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[text()='Payment Information']"))
        )

        if payment_info_label.is_displayed():
            driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")
            sys.exit(0)
        else:
            sys.exit(1)

    except Exception as e:
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")
        sys.exit(1)
    finally:
        driver.quit()

test_payment_information_visibility()
