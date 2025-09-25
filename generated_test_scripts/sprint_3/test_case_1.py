
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import sys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = "//input[@id='user-name']"
        self.password_input = "//input[@id='password']"
        self.login_button = "//input[@id='login-button']"

    def login(self, username, password):
        self.driver.find_element(By.XPATH, self.username_input).send_keys(username)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.password_input).send_keys(password)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.login_button).click()
        time.sleep(3)

def main():
    try:
        # Setup Chrome options
        chrome_options = Options()
        chrome_options.add_argument('--incognito')
        chrome_options.add_argument('--disable-notifications')
        chrome_options.add_argument('--disable-features=NetworkService')

        # Initialize WebDriver
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://saucedemo.com/')
        time.sleep(5)
        driver.maximize_window()

        # Login
        login_page = LoginPage(driver)
        login_page.login('standard', 'secret_sauce')

        # Add items to cart
        driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']").click()
        time.sleep(3)

        # Navigate to cart
        driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
        time.sleep(3)

        # Proceed to checkout
        driver.find_element(By.XPATH, "//button[@id='checkout']").click()
        time.sleep(3)

        # Enter shipping information
        driver.find_element(By.XPATH, "//input[@id='first-name']").send_keys('Jonnathan')
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='last-name']").send_keys('K')
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@id='postal-code']").send_keys('10007')
        time.sleep(3)

        # Continue and finish purchase
        driver.find_element(By.XPATH, "//input[@id='continue']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@id='finish']").click()
        time.sleep(3)

        # Return to homepage
        driver.find_element(By.XPATH, "//button[@id='back-to-products']").click()
        time.sleep(3)

        # Logout
        driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//a[@id='logout_sidebar_link']").click()
        time.sleep(3)

        # Test passed
        driver.save_screenshot(r'C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\success.png')
        driver.quit()
        sys.exit(0)
    except Exception as e:
        driver.save_screenshot(r'C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\failure.png')
        driver.quit()
        sys.exit(1)

if __name__ == '__main__':
    main()
