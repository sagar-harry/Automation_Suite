
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
            EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]'))
        )
        password_field = self.driver.find_element(By.XPATH, '//*[@id="password"]')
        login_button = self.driver.find_element(By.XPATH, '//*[@id="login-button"]')

        username_field.send_keys(username)
        password_field.send_keys(password)
        time.sleep(3)
        login_button.click()

def run_test():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=options)

    try:
        driver.maximize_window()
        driver.get('https://saucedemo.com/')
        time.sleep(5)

        login_page = LoginPage(driver)
        login_page.login('standard_user', 'secret_sauce')

        bike_light = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]'))
        )
        bike_light.click()
        time.sleep(3)

        fleece_jacket = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
        )
        fleece_jacket.click()
        time.sleep(3)

        cart_icon = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
        cart_icon.click()
        time.sleep(3)

        checkout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="checkout"]'))
        )
        checkout_button.click()
        time.sleep(3)

        first_name = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="first-name"]'))
        )
        last_name = driver.find_element(By.XPATH, '//*[@id="last-name"]')
        zip_code = driver.find_element(By.XPATH, '//*[@id="postal-code"]')

        first_name.send_keys('Jonnathan')
        last_name.send_keys('K')
        zip_code.send_keys('10007')
        time.sleep(3)

        continue_button = driver.find_element(By.XPATH, '//*[@id="continue"]')
        continue_button.click()
        time.sleep(3)

        payment_info = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]'))
        )

        assert payment_info.is_displayed(), "Payment information section is not displayed"
        
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot.png")
        sys.exit(0)
        
    except Exception as e:
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\screenshot.png")
        print(f"Test failed: {str(e)}")
        sys.exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    run_test()
