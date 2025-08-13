
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

class LoginPage:
    def login(self, driver, username, password):
        user_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@id='user-name']"))
        )
        user_input.send_keys(username)
        
        password_input = driver.find_element(By.XPATH, "//input[@id='password']")
        password_input.send_keys(password)
        
        login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
        login_button.click()
        time.sleep(3)

def run_test():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        driver.maximize_window()

        login_page = LoginPage()
        login_page.login(driver, "standard_user", "secret_sauce")

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']"))
        ).click()
        time.sleep(3)

        driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']").click()
        time.sleep(3)

        cart_badge = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[@class='shopping_cart_badge']"))
        )
        assert cart_badge.text == '2'

        driver.find_element(By.XPATH, "//button[@id='remove-sauce-labs-bike-light']").click()
        time.sleep(3)

        driver.find_element(By.XPATH, "//button[@id='remove-sauce-labs-fleece-jacket']").click()
        time.sleep(3)

        assert len(driver.find_elements(By.XPATH, "//span[@class='shopping_cart_badge']")) == 0

        driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']").click()
        time.sleep(3)

        cart_badge = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[@class='shopping_cart_badge']"))
        )
        assert cart_badge.text == '1'

        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")
        sys.exit(0)
    except Exception as e:
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    run_test()
