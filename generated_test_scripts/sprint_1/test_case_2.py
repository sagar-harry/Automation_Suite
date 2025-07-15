
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

class LoginPage:
    def login(self, driver, username, password):
        driver.find_element(By.ID, "user-name").send_keys(username)
        time.sleep(3)
        driver.find_element(By.ID, "password").send_keys(password)
        time.sleep(3)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(3)

def main():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://saucedemo.com/")
        time.sleep(5)
        driver.maximize_window()

        login_page = LoginPage()
        login_page.login(driver, "standard_user", "secret_sauce")

        bike_light_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bike-light"))
        )
        bike_light_button.click()
        time.sleep(3)

        fleece_jacket_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-fleece-jacket"))
        )
        fleece_jacket_button.click()
        time.sleep(3)

        checkout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout_button.click()
        time.sleep(3)

        driver.find_element(By.ID, "first-name").send_keys("Jonnathan")
        time.sleep(3)
        driver.find_element(By.ID, "last-name").send_keys("K")
        time.sleep(3)
        driver.find_element(By.ID, "postal-code").send_keys("10007")
        time.sleep(3)
        driver.find_element(By.ID, "continue").click()
        time.sleep(3)

        payment_information_label = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[text()='Payment Information']"))
        )

        if payment_information_label:
            driver.save_screenshot(
                r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png"
            )
            sys.exit(0)
    except Exception as e:
        driver.save_screenshot(
            r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\error_screenshot.png"
        )
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
