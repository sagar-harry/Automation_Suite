
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='user-name']")))
        password_field = self.driver.find_element(By.XPATH, "//input[@id='password']")
        login_button = self.driver.find_element(By.XPATH, "//input[@id='login-button']")
        
        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()

def main():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-features=NetworkService")
    
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://saucedemo.com/")
    time.sleep(5)

    try:
        page = LoginPage(driver)
        page.login('standard_user', 'secret_sauce')
        time.sleep(3)

        bike_light_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']"))
        )
        bike_light_btn.click()
        time.sleep(3)

        fleece_jacket_btn = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']")
        fleece_jacket_btn.click()
        time.sleep(3)

        cart_icon = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
        cart_icon.click()
        time.sleep(3)

        checkout = driver.find_element(By.XPATH, "//button[@id='checkout']")
        checkout.click()
        time.sleep(3)

        first_name = driver.find_element(By.NAME, "firstName")
        last_name = driver.find_element(By.NAME, "lastName")
        postal_code = driver.find_element(By.NAME, "postalCode")
        first_name.send_keys("Jonnathan")
        last_name.send_keys("K")
        postal_code.send_keys("10007")

        continue_btn = driver.find_element(By.XPATH, "//input[@id='continue']")
        continue_btn.click()
        time.sleep(3)

        finish_btn = driver.find_element(By.XPATH, "//button[@id='finish']")
        finish_btn.click()
        time.sleep(3)

        open_menu = driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']")
        open_menu.click()
        time.sleep(3)

        logout_link = driver.find_element(By.XPATH, "//a[@id='logout_sidebar_link']")
        logout_link.click()
        time.sleep(3)

        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")

    except Exception as e:
        print(e)
        driver.quit()
        sys.exit(1)

    driver.quit()
    sys.exit(0)

if __name__ == "__main__":
    main()
