
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]'))
        )
        password_field = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        login_button = self.driver.find_element(By.XPATH, '//*[@id="login-button"]')

        username_field.send_keys(username)
        time.sleep(3)
        password_field.send_keys(password)
        time.sleep(3)
        login_button.click()
        time.sleep(5)

def main():
    try:
        url = 'https://saucedemo.com/'
        username = 'standard_user'
        password = 'secret_sauce'

        options = Options()
        options.add_argument("--incognito")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-features=NetworkService")

        driver = webdriver.Chrome(options=options)
        driver.get(url)
        driver.maximize_window()
        time.sleep(5)

        login_page = LoginPage(driver)
        login_page.login(username, password)

        # Add 'Bike Light' and 'Fleece Jacket' to the cart
        bike_light = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
        )
        bike_light.click()
        time.sleep(3)

        fleece_jacket = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        fleece_jacket.click()
        time.sleep(3)

        # Go to cart
        cart_icon = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
        cart_icon.click()
        time.sleep(3)

        # Proceed to checkout
        checkout_button = driver.find_element(By.XPATH, '//*[@id="checkout"]')
        checkout_button.click()
        time.sleep(3)

        # Enter checkout information
        first_name_field = driver.find_element(By.XPATH, '//*[@id="first-name"]')
        last_name_field = driver.find_element(By.XPATH, '//*[@id="last-name"]')
        postal_code_field = driver.find_element(By.XPATH, '//*[@id="postal-code"]')
        first_name_field.send_keys('Jonnathan')
        time.sleep(3)
        last_name_field.send_keys('K')
        time.sleep(3)
        postal_code_field.send_keys('10007')
        time.sleep(3)

        # Click 'Continue' and complete the purchase
        continue_button = driver.find_element(By.XPATH, '//*[@id="continue"]')
        continue_button.click()
        time.sleep(3)

        finish_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="finish"]'))
        )
        finish_button.click()
        time.sleep(5)

        # Return to homepage
        back_to_products = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="back-to-products"]'))
        )
        back_to_products.click()
        time.sleep(5)

        # Logout
        logout_sidebar = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="react-burger-menu-btn"]'))
        )
        logout_sidebar.click()
        time.sleep(3)

        logout_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="logout_sidebar_link"]'))
        )
        logout_button.click()
        time.sleep(3)

        driver.save_screenshot('C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot.png')
        driver.quit()
        sys.exit(0)

    except Exception as e:
        driver.save_screenshot('C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot_error.png')
        driver.quit()
        sys.exit(1)

if __name__ == "__main__":
    main()
