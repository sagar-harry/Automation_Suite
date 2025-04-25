
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import sys
import time

def test_cart_updates_correctly():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popups")
    options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=options)
    driver.get("https://saucedemo.com/")
    driver.maximize_window()
    time.sleep(5)

    try:
        login(driver)
        time.sleep(3)

        bike_light = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
        )
        bike_light.click()
        time.sleep(3)

        fleece_jacket = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
        )
        fleece_jacket.click()
        time.sleep(3)

        cart_badge = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
        )

        assert cart_badge.text == '2', f"Expected cart count to be '2' but got {cart_badge.text}"
        sys.exit(0)

    except Exception as e:
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot.png")
        sys.exit(1)

    finally:
        driver.quit()

def login(driver):
    username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]'))
    )
    password = driver.find_element(By.XPATH, '//*[@id="password"]')

    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    
    login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')
    login_button.click()

if __name__ == "__main__":
    test_cart_updates_correctly()
