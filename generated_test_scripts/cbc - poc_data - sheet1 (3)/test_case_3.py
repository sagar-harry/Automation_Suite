
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def run_test():
    try:
        options = Options()
        options.headless = True
        options.add_argument('--disable-notifications')
        options.add_argument('--incognito')
        options.add_argument('--disable-features=NetworkService')

        driver = webdriver.Chrome(options=options)
        
        driver.get('https://practicetestautomation.com/practice-test-login/')
        time.sleep(5)
        driver.maximize_window()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='username']"))
        )

        username_field = driver.find_element(By.XPATH, "//input[@name='username']")
        password_field = driver.find_element(By.XPATH, "//input[@name='password']")
        submit_button = driver.find_element(By.XPATH, "//*[@id='submit']")
        
        time.sleep(3)
        username_field.send_keys('student')
        time.sleep(3)
        password_field.send_keys('incorrectPassword')
        time.sleep(3)
        submit_button.click()
        time.sleep(3)

        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='error']"))
        )

        assert error_message.text == "Your password is invalid!"
        driver.quit()
        sys.exit(0)
    except Exception as e:
        print(f'Test failed: {e}')
        driver.quit()
        sys.exit(1)

if __name__ == '__main__':
    run_test()
