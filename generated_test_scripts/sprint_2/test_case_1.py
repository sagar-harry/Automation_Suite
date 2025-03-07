
import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_locator = '//*[@id="user-name"]'
        self.password_locator = '//*[@id="password"]'
        self.login_button_locator = '//*[@id="login-button"]'

    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.username_locator)))
        self.driver.find_element(By.XPATH, self.username_locator).send_keys(username)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.password_locator).send_keys(password)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.login_button_locator).click()

def main():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-features=NetworkService")
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        driver.maximize_window()

        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
        time.sleep(3)

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="first-name"]')))
        driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys("Jonnathan")
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("K")
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("10007")
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="continue"]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="finish"]').click()
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="back-to-products"]')))
        driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]').click()

        sys.exit(0)

    except Exception as e:
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\final_state.png")
        print(e)
        sys.exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
