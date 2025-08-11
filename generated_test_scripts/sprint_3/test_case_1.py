
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = "//input[@id='user-name']"
        self.password_input = "//input[@id='password']"
        self.login_button = "//input[@id='login-button']"

    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.username_input)))
        self.driver.find_element(By.XPATH, self.username_input).send_keys(username)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.password_input).send_keys(password)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.login_button).click()
        time.sleep(3)

def main():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-features=NetworkService")
    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get("https://saucedemo.com/")
        driver.maximize_window()
        time.sleep(5)

        login_page = LoginPage(driver)
        login_page.login("standard", "secret_sauce")

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']")))
        driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']").click()
        time.sleep(3)

        driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']").click()
        time.sleep(3)

        driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
        time.sleep(3)

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@id='checkout']")))
        driver.find_element(By.XPATH, "//button[@id='checkout']").click()
        time.sleep(3)

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='first-name']")))
        driver.find_element(By.XPATH, "//input[@id='first-name']").send_keys("Jonnathan")
        time.sleep(3)

        driver.find_element(By.XPATH, "//input[@id='last-name']").send_keys("K")
        time.sleep(3)

        driver.find_element(By.XPATH, "//input[@id='postal-code']").send_keys("10007")
        time.sleep(3)

        driver.find_element(By.XPATH, "//input[@id='continue']").click()
        time.sleep(3)

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@id='finish']")))
        driver.find_element(By.XPATH, "//button[@id='finish']").click()
        time.sleep(3)

        driver.find_element(By.XPATH, "//button[@id='back-to-products']").click()
        time.sleep(3)

        driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']").click()
        time.sleep(3)

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@id='logout_sidebar_link']")))
        driver.find_element(By.XPATH, "//a[@id='logout_sidebar_link']").click()
        time.sleep(3)

        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")
        sys.exit(0)

    except Exception as e:
        print(f"Test failed due to: {str(e)}")
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\error_screenshot.png")
        sys.exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
