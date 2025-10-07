
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

def save_screenshot(driver, filename):
    driver.save_screenshot(filename)

def main():
    try:
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-features=NetworkService")

        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        driver.get("https://saucedemo.com/")
        time.sleep(5)  # Wait after opening page

        class LoginPage:
            def login(self, driver, username, password):
                user_field = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//input[@id='user-name']"))
                )
                pass_field = driver.find_element(By.XPATH, "//input[@id='password']")
                login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")

                user_field.send_keys(username)
                time.sleep(3)
                pass_field.send_keys(password)
                time.sleep(3)
                login_button.click()
                time.sleep(3)

        login_page = LoginPage()
        login_page.login(driver, "standard_user", "secret_sauce")

        add_bike_light = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']"))
        )
        add_bike_light.click()
        time.sleep(3)

        add_fleece_jacket = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']"))
        )
        add_fleece_jacket.click()
        time.sleep(3)

        cart_icon = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
        cart_icon.click()
        time.sleep(3)

        checkout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='checkout']"))
        )
        checkout_button.click()
        time.sleep(3)

        driver.find_element(By.XPATH, "//input[@id='first-name']").send_keys("Jonnathan")
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='last-name']").send_keys("K")
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='postal-code']").send_keys("10007")
        time.sleep(3)

        continue_button = driver.find_element(By.XPATH, "//input[@id='continue']")
        continue_button.click()
        time.sleep(3)

        finish_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='finish']"))
        )
        finish_button.click()
        time.sleep(3)

        login_page.login(driver, "standard_user", "secret_sauce")
        
        open_menu = driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']")
        open_menu.click()
        time.sleep(3)

        logout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@id='logout_sidebar_link']"))
        )
        logout_button.click()
        
        save_screenshot(driver, r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")

        driver.quit()
        sys.exit(0)
    except Exception as e:
        save_screenshot(driver, r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")
        driver.quit()
        sys.exit(1)
        
if __name__ == "__main__":
    main()
