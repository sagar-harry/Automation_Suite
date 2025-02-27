
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

class LoginPage:
    def login(self, driver, username, password):
        driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(username)
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
        time.sleep(3)

def main():
    try:
        options = Options()
        options.add_argument("--incognito")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-features=NetworkService")

        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get("https://saucedemo.com/")
        time.sleep(5)

        wait = WebDriverWait(driver, 10)

        login_page = LoginPage()
        login_page.login(driver, "standard_user", "secret_sauce")

        bike_light = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')))
        bike_light.click()
        time.sleep(3)

        fleece_jacket = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')))
        fleece_jacket.click()
        time.sleep(3)

        cart_icon = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="shopping_cart_container"]/a')))
        cart_icon.click()
        time.sleep(3)

        checkout_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="checkout"]')))
        checkout_button.click()
        time.sleep(3)

        first_name = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="first-name"]')))
        first_name.send_keys("somename")
        time.sleep(3)

        last_name = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="last-name"]')))
        last_name.send_keys("lastname")
        time.sleep(3)

        zip_code = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="postal-code"]')))
        zip_code.send_keys("123456")
        time.sleep(3)

        continue_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="continue"]')))
        continue_button.click()
        time.sleep(3)

        payment_info = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[1]')))

        if payment_info.is_displayed():
            driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\success.png")
            sys.exit(0)
        else:
            driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\failure.png")
            sys.exit(1)

    except Exception as e:
        driver.save_screenshot("C:\\Users\\Administrator\\Desktop\\QE_COE\\automated_pipeline_2\\captured_screenshots\\error.png")
        sys.exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
