
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys(username)
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)
        self.driver.find_element(By.XPATH, "//input[@id='login-button']").click()

def main():
    try:
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-features=NetworkService")

        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.get("https://saucedemo.com/")
        time.sleep(5)

        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        time.sleep(3)  # wait before next action

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']")))
        driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']").click()
        time.sleep(3)
        
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']")))
        driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']").click()
        time.sleep(3)

        cart_badge = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='shopping_cart_badge']")))
        assert cart_badge.text == '2', "Cart badge does not display '2'"

        driver.find_element(By.XPATH, "//button[@id='remove-sauce-labs-bike-light']").click()
        time.sleep(3)

        driver.find_element(By.XPATH, "//button[@id='remove-sauce-labs-fleece-jacket']").click()
        time.sleep(3)

        try:
            cart_badge = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
            assert False, "Cart count element should not exist"
        except:
            pass
        
        driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']").click()
        time.sleep(3)

        cart_badge = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='shopping_cart_badge']")))
        assert cart_badge.text == '1', "Cart badge does not display '1'"

        with open(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png", "wb") as file:
            file.write(driver.get_screenshot_as_png())

        driver.quit()
        sys.exit(0)

    except Exception as e:
        with open(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\error_screenshot.png", "wb") as file:
            file.write(driver.get_screenshot_as_png())

        driver.quit()
        sys.exit(1)

if __name__ == "__main__":
    main()
