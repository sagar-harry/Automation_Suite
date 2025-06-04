
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
        user_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'user-name'))
        )
        user_input.send_keys(username)
        password_input = self.driver.find_element(By.ID, 'password')
        password_input.send_keys(password)
        login_button = self.driver.find_element(By.ID, 'login-button')
        login_button.click()

def run_test():
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-features=NetworkService")
        
        driver = webdriver.Chrome(chrome_options=options)
        driver.get("https://www.saucedemo.com/")
        
        time.sleep(5)  # Wait for 5 secs after opening the page
        driver.maximize_window()
        
        # Log in to the website
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        time.sleep(3)  # Wait for 3 secs before each action

        # Add 'Bike Light' to cart
        bike_light_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'add-to-cart-sauce-labs-bike-light'))
        )
        bike_light_button.click()

        time.sleep(3)  # Wait for 3 secs

        # Add 'Fleece Jacket' to cart
        fleece_jacket_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'add-to-cart-sauce-labs-fleece-jacket'))
        )
        fleece_jacket_button.click()

        time.sleep(3)  # Wait for 3 secs

        # Proceed to checkout
        cart_button = driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
        cart_button.click()

        time.sleep(3)  # Wait for 3 secs

        checkout_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'checkout'))
        )
        checkout_button.click()

        time.sleep(3)  # Wait for 3 secs

        # Enter checkout information
        first_name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'first-name'))
        )
        first_name_input.send_keys("Jonnathan")

        last_name_input = driver.find_element(By.ID, 'last-name')
        last_name_input.send_keys("K")

        postal_code_input = driver.find_element(By.ID, 'postal-code')
        postal_code_input.send_keys("10007")

        time.sleep(3)  # Wait for 3 secs

        continue_button = driver.find_element(By.ID, 'continue')
        continue_button.click()

        time.sleep(3)  # Wait for 3 secs

        # Verify payment information label is visible
        payment_info_label = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h1[text()='Payment Information']"))
        )

        assert payment_info_label.is_displayed(), "Payment Information label not visible"

        # Save screenshot if successful
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\page_snapshot.png")
        
        driver.quit()
        sys.exit(0)

    except Exception as e:
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\page_snapshot.png")
        driver.quit()
        sys.exit(1)

if __name__ == "__main__":
    run_test()
