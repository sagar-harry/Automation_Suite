
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import sys
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]'))).send_keys(username)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]'))).send_keys(password)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login-button"]'))).click()

def main():
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://saucedemo.com/")
    time.sleep(5)
    driver.maximize_window()

    try:
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        time.sleep(3)
        bike_light_button = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
        bike_light_button.click()

        time.sleep(3)
        fleece_jacket_button = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]')))
        fleece_jacket_button.click()

        time.sleep(3)
        cart_badge = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
        assert cart_badge.text == '2', "Cart badge should display '2'"

        time.sleep(3)
        remove_bike_light_button = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="remove-sauce-labs-bike-light"]')))
        remove_bike_light_button.click()

        time.sleep(3)
        remove_fleece_jacket_button = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="remove-sauce-labs-fleece-jacket"]')))
        remove_fleece_jacket_button.click()

        time.sleep(3)
        cart_count_elements = driver.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        assert len(cart_count_elements) == 0, "Cart count element shouldn't exist"

        time.sleep(3)
        add_bolt_tshirt_button = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')))
        add_bolt_tshirt_button.click()

        time.sleep(3)
        cart_badge = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="shopping_cart_container"]/a/span')))
        assert cart_badge.text == '1', "Cart badge should display '1'"

        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")
        sys.exit(0)

    except Exception as e:
        print(f"Test failed due to: {e}")
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")
        sys.exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
