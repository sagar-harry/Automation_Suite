
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_invalid_login():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('--disable-features=NetworkService')

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    try:
        driver.get('https://practicetestautomation.com/practice-test-login/')
        time.sleep(5)

        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='username']"))
        )
        time.sleep(3)
        username_field.send_keys('incorrectUser')

        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='password']"))
        )
        time.sleep(3)
        password_field.send_keys('Password123')

        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='submit']"))
        )
        time.sleep(3)
        submit_button.click()

        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[text()='Your username is invalid!']"))
        )

        if error_message.is_displayed():
            sys.exit(0)
        else:
            sys.exit(1)
    except Exception as e:
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == '__main__':
    test_invalid_login()
