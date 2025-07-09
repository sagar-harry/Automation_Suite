
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

class LoginPage:
    def login(self, driver, username, password):
        username_field = driver.find_element(By.ID, 'user-name')
        password_field = driver.find_element(By.ID, 'password')
        login_button = driver.find_element(By.ID, 'login-button')

        username_field.send_keys(username)
        time.sleep(3)
        password_field.send_keys(password)
        time.sleep(3)
        login_button.click()
        time.sleep(3)

def main():
    url = "https://saucedemo.com/"
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(url)
    time.sleep(5)

    try:
        login_page = LoginPage()
        login_page.login(driver, "standard_user", "secret_sauce")

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'add-to-cart-sauce-labs-bike-light'))
        ).click()
        time.sleep(3)

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'add-to-cart-sauce-labs-fleece-jacket'))
        ).click()
        time.sleep(3)

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'checkout'))
        ).click()
        time.sleep(3)

        first_name_field = driver.find_element(By.ID, 'first-name')
        last_name_field = driver.find_element(By.ID, 'last-name')
        postal_code_field = driver.find_element(By.ID, 'postal-code')
        continue_button = driver.find_element(By.ID, 'continue')

        first_name_field.send_keys('Jonnathan')
        time.sleep(3)
        last_name_field.send_keys('K')
        time.sleep(3)
        postal_code_field.send_keys('10007')
        time.sleep(3)
        continue_button.click()
        time.sleep(3)

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='summary_info_label' and text()='Payment Information']"))
        )

        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\screenshot.png")
        sys.exit(0)
    except Exception as e:
        driver.save_screenshot(r"C:\Users\Administrator\Desktop\QE_COE\automated_pipeline_2\captured_screenshots\error_screenshot.png")
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
