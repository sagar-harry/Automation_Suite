
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    
    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]'))
        ).send_keys(username)
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
        time.sleep(3)

def main():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-features=NetworkService")
    
    driver = webdriver.Chrome(options=options)

    try:
        driver.maximize_window()
        driver.get("https://saucedemo.com/")
        time.sleep(5)

        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
        ).click()
        time.sleep(3)

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
        ).click()
        time.sleep(3)

        cart_count = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span'))
        ).text

        if cart_count == '2':
            print("Test case passed")
            sys.exit(0)
        else:
            print("Test case failed")
            sys.exit(1)

    except Exception as e:
        print(f"An error occurred: {e}")
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\error.png")
        sys.exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
