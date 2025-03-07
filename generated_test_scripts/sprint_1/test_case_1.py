
import time
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_locator = "//*[@id='user-name']"
        self.password_locator = "//*[@id='password']"
        self.login_button_locator = "//*[@id='login-button']"

    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.username_locator)))
        self.driver.find_element(By.XPATH, self.username_locator).send_keys(username)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.password_locator).send_keys(password)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.login_button_locator).click()
        time.sleep(3)

def main():
    try:
        options = Options()
        options.add_argument('--disable-notifications')
        options.add_argument('--disable-popup-blocking')
        options.add_argument('--incognito')
        options.add_argument('--disable-features=NetworkService')

        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get("https://saucedemo.com/")
        time.sleep(5)

        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']")))
        driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']").click()
        time.sleep(3)

        driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-fleece-jacket']").click()
        time.sleep(3)

        cart_count = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='shopping_cart_container']/a/span")))
        assert cart_count.text == '2', f"Expected cart count '2', but got {cart_count.text}"

        driver.find_element(By.XPATH, "//*[@id='remove-sauce-labs-bike-light']").click()
        time.sleep(3)

        driver.find_element(By.XPATH, "//*[@id='remove-sauce-labs-fleece-jacket']").click()
        time.sleep(3)

        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.XPATH, "//*[@id='shopping_cart_container']/a/span")))

        driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']").click()
        time.sleep(3)

        cart_count = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='shopping_cart_container']/a/span")))
        assert cart_count.text == '1', f"Expected cart count '1', but got {cart_count.text}"

        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")
        driver.quit()
        sys.exit(0)
    except Exception as e:
        print(f"Test failed: {e}")
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\error_screenshot.png")
        driver.quit()
        sys.exit(1)

if __name__ == "__main__":
    main()
