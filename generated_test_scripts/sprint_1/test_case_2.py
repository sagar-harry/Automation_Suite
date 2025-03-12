
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]'))
        ).send_keys(username)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))
        ).send_keys(password)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="login-button"]'))
        ).click()

def run_test_case():
    try:
        options = Options()
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--incognito")
        options.add_argument("--disable-features=NetworkService")

        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get("https://saucedemo.com/")
        time.sleep(5)

        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
        ).click()

        time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
        ).click()

        time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a'))
        ).click()

        time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="checkout"]'))
        ).click()

        time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="first-name"]'))
        ).send_keys("Jonnathan")

        time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="last-name"]'))
        ).send_keys("K")

        time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="postal-code"]'))
        ).send_keys("10007")

        time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="continue"]'))
        ).click()

        time.sleep(3)
        payment_info_visible = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]'))
        ).is_displayed()

        if payment_info_visible:
            print("Test Case Passed")
            sys.exit(0)
        else:
            print("Test Case Failed")
            sys.exit(1)

    except Exception as e:
        print(f"Test Case Failed: {str(e)}")
        sys.exit(1)

    finally:
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")
        driver.quit()

if __name__ == "__main__":
    run_test_case()
