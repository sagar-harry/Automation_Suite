
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def run_test():
    options = Options()
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--incognito")
    options.add_argument("--disable-features=NetworkService")

    driver = webdriver.Chrome(options=options)

    try:
        driver.maximize_window()
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(5)

        wait = WebDriverWait(driver, 10)

        username_field = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='username']")))
        time.sleep(3)
        username_field.send_keys("incorrectUser")

        password_field = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='password']")))
        time.sleep(3)
        password_field.send_keys("Password123")

        submit_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='submit']")))
        time.sleep(3)
        submit_button.click()

        error_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[text()='Your username is invalid!']")))
        time.sleep(3)

        if error_message.is_displayed():
            sys.exit(0)
        else:
            sys.exit(1)
    except Exception as e:
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    run_test()
