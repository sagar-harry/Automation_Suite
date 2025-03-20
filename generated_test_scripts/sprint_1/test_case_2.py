
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()

def run_test():
    try:
        options = Options()
        options.add_argument("--incognito")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-features=NetworkService")

        driver = webdriver.Chrome(options=options)
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        driver.maximize_window()

        login_page = LoginPage(driver)
        login_page.login('standard_user', 'secret_sauce')

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
        ).send_keys('Jonnathan')

        time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="last-name"]'))
        ).send_keys('K')

        time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="postal-code"]'))
        ).send_keys('10007')

        time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="continue"]'))
        ).click()

        time.sleep(3)
        payment_info_visible = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]'))
        )

        snapshot_path = r'C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png'
        driver.save_screenshot(snapshot_path)

        if payment_info_visible:
            sys.exit(0)
        else:
            sys.exit(1)

    except Exception as e:
        driver.save_screenshot(r'C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\error_screenshot.png')
        print(f"Test failed due to: {e}")
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    run_test()
